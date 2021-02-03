# run this program on the Mac to display image streams from multiple RPis
import sys
import cv2
import requests
import json
import imagezmq
import os
import time
from PIL import Image
import face_recognition
import pickle
import io
#addr = 'http://192.168.0.22:5000'
addr = 'http://127.0.0.1:8000/'
test_url = addr + 'api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}


def processImage(frame):
    face_locations = face_recognition.face_locations(frame)
    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
            top, left, bottom, right))
    # You can access the actual face itself like this:
        face_image = frame[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        # msg = pickle.dumps(pil_image)

        file_like_object = io.BytesIO()
        pil_image.save(file_like_object, format='jpeg')

        #_, img_encoded = cv2.imencode('.jpg', pil_image)
        # send http request with image and receive response
        try:
            response = requests.post(
                test_url, data=file_like_object.getvalue(), headers=headers)
            print(json.loads(response.text))
        except requests.exceptions.HTTPError as e:
            print("Error: " + str(e))
        # decode response

        # pil_image.show()
        image = pil_image
        # pil_image.delete()


    # Create a hub for receiving images from cameras
image_hub = imagezmq.ImageHub()

# Create a PUB server to send images for monitoring purposes in a non-blocking mode
# stream_monitor = imagezmq.ImageSender(
#   connect_to='tcp://*:5566', REQ_REP=False)  # to enalbe server
#

# Start main loop
while True:
    rpi_name, image = image_hub.recv_image()
    image_hub.send_reply(b'OK')
    processImage(image)
    #cv2.imshow(rpi_name, image)
    #stream_monitor.send_image(rpi_name, image)


# from __future__ import print_function
# import requests
# import json
# import cv2

# addr = 'http://192.168.0.22:5000'
# test_url = addr + '/api/test'

# # prepare headers for http request
# content_type = 'image/jpeg'
# headers = {'content-type': content_type}

# img = cv2.imread('lena.jpg')
# # encode image as jpeg
# _, img_encoded = cv2.imencode('.jpg', img)
# # send http request with image and receive response
# response = requests.post(
#     test_url, data=img_encoded.tostring(), headers=headers)
# # decode response
# print(json.loads(response.text))


# # run this program on the Mac to display image streams from multiple RPis
# import sys
# import cv2
# import imagezmq
# import cv2 as cv
# import os
# import time
# from PIL import Image
# import face_recognition


# def processImage(frame):
#     face_locations = face_recognition.face_locations(frame)
#     print("I found {} face(s) in this photograph.".format(len(face_locations)))
#     for face_location in face_locations:
#         # Print the location of each face in this image
#         top, right, bottom, left = face_location
#         print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(
#             top, left, bottom, right))
#     # You can access the actual face itself like this:
#         face_image = frame[top:bottom, left:right]
#         pil_image = Image.fromarray(face_image)
#         pil_image.show()
#         image = pil_image
#         # pil_image.delete()

#     # Create a hub for receiving images from cameras
# image_hub = imagezmq.ImageHub()

# # Create a PUB server to send images for monitoring purposes in a non-blocking mode
# # stream_monitor = imagezmq.ImageSender(
# #   connect_to='tcp://*:5566', REQ_REP=False)  # to enalbe server
# #

# # Start main loop
# while True:
#     rpi_name, image = image_hub.recv_image()
#     image_hub.send_reply(b'OK')
#     processImage(image)
#     #cv2.imshow(rpi_name, image)
#     #stream_monitor.send_image(rpi_name, image)
