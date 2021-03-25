

import os
from pathlib import Path
import cv2
import requests
import json
size = 4


dirname, filename = os.path.split(os.path.abspath(__file__))
# print(BASE_DIR)
# model = os.path.join(BASE_DIR, "\CMPRS\model\haarcascade_frontalface_alt.xml")
model = dirname+"\model\haarcascade_frontalface_alt.xml"
# print(BASE_DIR)
# print(model)
# face_route = os.path.join(BASE_DIR, "/CMPRS/unknowfaces")
face_route = dirname+"\\unknowfaces"
print(face_route)
webcam = cv2.VideoCapture(
    "rtsp://192.168.0.10:8080/h264_ulaw.sdp")
addr = 'http://127.0.0.1:8000/'
test_url = addr + 'api/test/'

# classifier = cv2.CascadeClassifier("rtsp://192.168.0.11:8080/h264_ulaw.sdp")

classifier = cv2.CascadeClassifier(model)


while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  # Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))

    faces = classifier.detectMultiScale(mini)

    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), thickness=4)
        # Save just the rectangle faces in SubRecFaces
        sub_face = im[y:y+h, x:x+w]
        FaceFileName = face_route+"/face_" + str(y) + ".jpg"
        cv2.imwrite(FaceFileName, sub_face)
        files = {'image': open(FaceFileName, 'rb')}
        try:
            response = requests.post(test_url, files=files)
            print(json.loads(response.text))
        except requests.exceptions.HTTPError as e:
            print("Error: " + str(e))

    # Show the image
    cv2.imshow('System',   im)
    key = cv2.waitKey(10)
    # if Esc key is press then break out of the loop
    if key == 27:  # The Esc key
        break
