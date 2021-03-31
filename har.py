

# import cv2
# size = 4
# webcam = cv2.VideoCapture(
#     "rtsp://192.168.0.12:8080/h264_ulaw.sdp")  # Use camera

# # We load the xml file
# # classifier = cv2.CascadeClassifier("rtsp://192.168.0.11:8080/h264_ulaw.sdp")
# # #  Above line normalTest
# classifier = cv2.CascadeClassifier(
#     'f:/project-final/CMPRS/model/haarcascade_frontalface_alt.xml')
# # Above line test with different calulation
# #classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
# #classifier = cv2.CascadeClassifier('lbpcascade_frontalface.xml')


# while True:
#     (rval, im) = webcam.read()
#     im = cv2.flip(im, 1, 0)  # Flip to act as a mirror

#     # Resize the image to speed up detection
#     mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))

#     # detect MultiScale / faces
#     faces = classifier.detectMultiScale(mini)

#     # Draw rectangles around each face
#     for f in faces:
#         (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
#         cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), thickness=4)
#         # Save just the rectangle faces in SubRecFaces
#         sub_face = im[y:y+h, x:x+w]
#         FaceFileName = "f:/project-final/CMPRS/unknowfaces/face_" + \
#             str(y) + ".jpg"
#         cv2.imwrite(FaceFileName, sub_face)

#     # Show the image
#     cv2.imshow('see',   im)
#     key = cv2.waitKey(10)
#     # if Esc key is press then break out of the loop
#     if key == 27:  # The Esc key
#         break

# import cv2
# #import the cascade for face detection
# FaceClassifier =cv2.CascadeClassifier
# ('haarcascade_frontalface_default.xml')
# # access the webcam (every webcam has
# capture = cv2.VideoCapture(0)

# while(True):
#     ret, frame = capture.read()
#     if not capture:
#       print("Error opening webcam device")
#       sys.exit(1)


#     # to detect faces in video
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = FaceClassifier.detectMultiScale(gray, 1.3, 5)

#     # Resize Image
#     minisize = (frame.shape[1],frame.shape[0])
#     miniframe = cv2.resize(frame, minisize)
#     # Store detected frames in variable name faces
#    faces =  FaceClassifier.detectMultiScale(miniframe)
#    # Draw rectangle
#    for f in faces:
#       x, y, w, h = [ v for v in f ]
#       cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255))
#     #Save just the rectangle faces in SubRecFaces
#     sub_face = frame[y:y+h, x:x+w]
#     FaceFileName = "unknowfaces/face_" + str(y) + ".jpg"
#     cv2.imwrite(FaceFileName, sub_face)
#     #Display the image
#     cv2.imshow('Result',frame)


#     break

#     # When everything done, release the capture

#     img.release()
#     cv2.waitKey(20)
#     cv2.destroyAllWindows()
# import cv2  # Opencv
# import Image  # Image from PIL
# import glob
# import os


# def DetectFace(image, faceCascade, returnImage=False):
#     # This function takes a grey scale cv image and finds
#     # the patterns defined in the haarcascade function
#     # modified from: http://www.lucaamore.com/?p=638

#     # variables
#     min_size = (20, 20)
#     haar_scale = 1.1
#     min_neighbors = 3
#     haar_flags = 0

#     # Equalize the histogram
#     cv.EqualizeHist(image, image)

#     # Detect the faces
#     faces = cv.HaarDetectObjects(
#         image, faceCascade, cv.CreateMemStorage(0),
#         haar_scale, min_neighbors, haar_flags, min_size
#     )

#     # If faces are found
#     if faces and returnImage:
#         for ((x, y, w, h), n) in faces:
#             # Convert bounding box to two CvPoints
#             pt1 = (int(x), int(y))
#             pt2 = (int(x + w), int(y + h))
#             cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 5, 8, 0)

#     if returnImage:
#         return image
#     else:
#         return faces


# def pil2cvGrey(pil_im):
#     # Convert a PIL image to a greyscale cv image
#     # from: http://pythonpath.wordpress.com/2012/05/08/pil-to-opencv-image/
#     pil_im = pil_im.convert('L')
#     cv_im = cv.CreateImageHeader(pil_im.size, cv.IPL_DEPTH_8U, 1)
#     cv.SetData(cv_im, pil_im.tostring(), pil_im.size[0])
#     return cv_im


# def cv2pil(cv_im):
#     # Convert the cv image to a PIL image
#     return Image.fromstring("L", cv.GetSize(cv_im), cv_im.tostring())


# def imgCrop(image, cropBox, boxScale=1):
#     # Crop a PIL image with the provided box [x(left), y(upper), w(width), h(height)]

#     # Calculate scale factors
#     xDelta = max(cropBox[2]*(boxScale-1), 0)
#     yDelta = max(cropBox[3]*(boxScale-1), 0)

#     # Convert cv box to PIL box [left, upper, right, lower]
#     PIL_box = [cropBox[0]-xDelta, cropBox[1]-yDelta, cropBox[0] +
#                cropBox[2]+xDelta, cropBox[1]+cropBox[3]+yDelta]

#     return image.crop(PIL_box)


# def faceCrop(imagePattern, boxScale=1):
#     # Select one of the haarcascade files:
#     #   haarcascade_frontalface_alt.xml  <-- Best one?
#     #   haarcascade_frontalface_alt2.xml
#     #   haarcascade_frontalface_alt_tree.xml
#     #   haarcascade_frontalface_default.xml
#     #   haarcascade_profileface.xml
#     faceCascade = cv.Load('haarcascade_frontalface_alt.xml')

#     imgList = glob.glob(imagePattern)
#     if len(imgList) <= 0:
#         print('No Images Found')
#         return

#     for img in imgList:
#         pil_im = Image.open(img)
#         cv_im = pil2cvGrey(pil_im)
#         faces = DetectFace(cv_im, faceCascade)
#         if faces:
#             n = 1
#             for face in faces:
#                 croppedImage = imgCrop(pil_im, face[0], boxScale=boxScale)
#                 fname, ext = os.path.splitext(img)
#                 croppedImage.save(fname+'_crop'+str(n)+ext)
#                 n += 1
#         else:
#             print('No faces found:' + img)


# def test(imageFilePath):
#     pil_im = Image.open(imageFilePath)
#     cv_im = pil2cvGrey(pil_im)
#     # Select one of the haarcascade files:
#     #   haarcascade_frontalface_alt.xml  <-- Best one?
#     #   haarcascade_frontalface_alt2.xml
#     #   haarcascade_frontalface_alt_tree.xml
#     #   haarcascade_frontalface_default.xml
#     #   haarcascade_profileface.xml
#     faceCascade = cv.Load('haarcascade_frontalface_alt.xml')
#     face_im = DetectFace(cv_im, faceCascade, returnImage=True)
#     img = cv2pil(face_im)
#     img.show()
#     img.save('test.png')


# # Test the algorithm on an image
# # test('testPics/faces.jpg')

# # Crop all jpegs in a folder. Note: the code uses glob which follows unix shell rules.
# # Use the boxScale to scale the cropping area. 1=opencv box, 2=2x the width and height
# faceCrop('testPics/*.jpg', boxScale=1)
