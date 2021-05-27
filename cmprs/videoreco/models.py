from django.db import models
from faceuploader.models import Face_image
# Create your models here.
import face_recognition
import cv2
import os

from datetime import datetime, timedelta


def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)


class Video_File(models.Model):
    case_name = models.CharField(max_length=30)
    video = models.FileField(upload_to="video_file")
    v_location = models.CharField(max_length=30, default='No location given')
    case_details = models.TextField(
        max_length=60, default="No case data givem")
    start_time = models.DateTimeField(default=default_start_time)
    end_time = models.DateTimeField(default=default_start_time)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        video_anlyser(self)

    def __str__(self):
        return f"{self.video}"


class Person(models.Model):
    person_image = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True)
    video_id = models.ForeignKey(
        Video_File, on_delete=models.CASCADE
    )

    created = models.DateTimeField(auto_now_add=True)
    person_id = models.ForeignKey(Face_image, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

    # def __str__(self):
    #     return f"{self.video_id}+{self.person_id}"


dirname, filename = os.path.split(os.path.abspath(__file__))
model1 = dirname+"\model\haarcascade_frontalface_alt.xml"
model2 = "f:\project-final\CMPRS\model\haarcascade_frontalface_alt.xml"
size = 6
face_route = dirname+"\\unknowfacesto"
classifier = cv2.CascadeClassifier(model2)


def video_anlyser(v):
    images = []
    encodings = []
    names = []
    files = []
    ids = []
    prsn = Face_image.objects.all()
    for crime in prsn:
        images.append(crime.name+'_image')
        encodings.append(crime.name+'_face_encoding')
        files.append(crime.photo)
        ids.append(crime.id)
        names.append('Name: '+crime.name)
    for i in range(0, len(images)):
        images[i] = face_recognition.load_image_file(files[i])
        encodings[i] = face_recognition.face_encodings(images[i])[0]
        print("####################")
        print(type(encodings))
        print("####################")
    NAME = "Unknown"
    known_face_encodings = encodings
    known_face_names = names
    print("inside####################anlyser")
    print(face_route)
    print(v.video.url)

    input_movie = cv2.VideoCapture('f:/project-final/CMPRS/cmprs/'+v.video.url)
    # print("##########test")
    print(input_movie)
    print('#############dir###########')
    print("dirname "+face_route)
    # input_movie = cv2.imdecode(v, cv2.IMREAD_COLOR)
    while True:
        (rval, im) = input_movie.read()
        # cv2.imshow('System',   im)
        im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
        try:
            mini = cv2.resize(
                im, (int(im.shape[1] / size), int(im.shape[0] / size)))
        except AttributeError:
            break
        faces = classifier.detectMultiScale(mini)
        for f in faces:
            (x, y, w, h) = [v * size for v in f]  #
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), thickness=4)
            sub_face = im[y:y+h, x:x+w]
            FaceFileName = 'f:/project-final/CMPRS/cmprs/media/unknown' + \
                "/face_" + str(y) + ".jpg"
            cv2.imwrite(FaceFileName, sub_face)
            f = open(FaceFileName, 'rb')
            print(f)
            # p = Person(person_image=FaceFileName, video_id=v)
            print('  # P OBJEcT####################')

            #############################################################
            img = face_recognition.load_image_file(f)
            unknown_face_encodings = face_recognition.face_encodings(img)
            face_found = False
            is_obama = False
            if len(unknown_face_encodings) > 0:
                face_found = True
                for face_encoding, know_face_name, ij in zip(known_face_encodings, known_face_names, prsn):
                    match_results = face_recognition.compare_faces(
                        [face_encoding], unknown_face_encodings[0])
                    if match_results[0]:
                        is_obama = True
                        NAME = know_face_name
                        find_id = ij
            if(is_obama):
                p = Person(person_image=FaceFileName,
                           person_id=find_id, video_id=v)
                print("#$$$$$#$$$$$$$$$$$$$$$")
                print(find_id)
                p.save()

            ###############

        cv2.imshow('System',   im)
        key = cv2.waitKey(10)
    print("video analyse finished")

    # class Recognized_Person(models.Model):
    #     reco_person_image = models.ImageField(
    #         upload_to='reco_photo/%Y/%m/%d/', null=True)
    #     video_id_r = models.ForeignKey(
    #         Video_File, on_delete=models.CASCADE
    #     )
    #     face_id = models.ForeignKey(
    #         Face_image, on_delete=models.CASCADE
    #     )

    #     created = models.DateTimeField(auto_now_add=True)
