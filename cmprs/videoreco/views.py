import threading
import os
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Video_File, Person
from .forms import Video_File_Form
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import face_recognition
import cv2
# Create your views here.


def video_uploader_index(request):
    video_files = Video_File.objects.all()
    return render(request, 'videoreco/main.html', {'video_files': video_files})


def create_video_uploader(request):
    if request.method == 'POST':
        video_uploader_form = Video_File_Form(request.POST, request.FILES)
        if video_uploader_form.is_valid():
            # length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
            # fourcc = cv2.VideoWriter_fourcc(*'XVID')
            # output_movie = cv2.VideoWriter('output.avi', fourcc, 29.97, (640, 360))
            # video_anlyser(video_r)
            video_uploader_form.save()
            return redirect('videoreco:index')
    else:
        video_uploader_form = Video_File_Form()
        return render(request, 'videoreco/create_video_uploader.html', {'video_uploader_form': video_uploader_form})


def detail_video_uploader(request, pk):
    video_file = get_object_or_404(Video_File, pk=pk)
    reco_face = Person.objects.filter(video_id=video_file)

    print(reco_face)
    # if reco_face.count() == 0:
    #     confirm = True
    # else:
    #     confirm = False
    return render(request, 'videoreco/detail_video.html', {'video_file': video_file, 'reco_face': reco_face})


def update_video(request, pk):
    video_file = get_object_or_404(Video_File, pk=pk)
    if request.method == "POST":
        video_uploader_form = Video_File_Form(
            request.POST, instance=video_file)
        if video_uploader_form.is_valid():
            video_uploader_form.save()
            return redirect('videoreco:index')
    else:
        video_uploader_form = Video_File_Form(instance=video_file)

    return render(
        request, 'videoreco/create_video_uploader.html',
        {
            'video_uploader_form': video_uploader_form
        }
    )


def delete_video_uploader(request, pk):
    video_file = get_object_or_404(Video_File, pk=pk)

    if video_file:
        video_file.delete()
    return redirect('videoreco:index')


# def detail_video_anlyser(request, pk):
#     video_file = get_object_or_404(Video_File, pk=pk)
#     #fire_and_forget(str(video_file.video.url), str(video_file))
#     video_anlyser(video_file.video.url, video_file)
#     return render(request, 'videoreco/detail_video.html', {'video_file': video_file})


# dirname, filename = os.path.split(os.path.abspath(__file__))
# model1 = dirname+"\model\haarcascade_frontalface_alt.xml"
# model2 = "f:\project-final\CMPRS\model\haarcascade_frontalface_alt.xml"
# size = 6
# face_route = dirname+"\\unknowfacesto"
# classifier = cv2.CascadeClassifier(model2)


# def fire_and_forget(v, video_file):
#     print("##################inside thread")
#     print(v)
#     threading.Thread(target=video_anlyser, args=(v, video_file)).start()


# def video_anlyser(v, video_file):
#     print(v)
#     print("f:/project-final/CMPRS/cmprs"+v)
#     # input_movie = cv2.VideoCapture(
#     #     "f:\project-final\CMPRS\cmprs\media\\video_file\WhatsApp_Video_2021-05-25_at_8.34.05_PM_1_8xlcoiV.mp4")
#     input_movie = cv2.VideoCapture("f:/project-final/CMPRS/cmprs"+v)
#     print("##########test")
#     print(input_movie)
#     # input_movie = cv2.imdecode(v, cv2.IMREAD_COLOR)
#     while True:
#         (rval, im) = input_movie.read()
#         # cv2.imshow('System',   im)
#         im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
#         try:
#             mini = cv2.resize(
#                 im, (int(im.shape[1] / size), int(im.shape[0] / size)))
#         except AttributeError:
#             break
#         faces = classifier.detectMultiScale(mini)
#         for f in faces:
#             (x, y, w, h) = [v * size for v in f]  #
#             cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), thickness=4)
#             sub_face = im[y:y+h, x:x+w]
#             FaceFileName = face_route+"\\face_" + str(y) + ".jpg"
#             cv2.imwrite(FaceFileName, sub_face)
#             f = open(FaceFileName, 'rb')
#             print(f)
#             p = Person(person_image=f, video_id=video_file)
#             p.save()
#         cv2.imshow('System',   im)
#         key = cv2.waitKey(10)
#     print("video analyse finished")
    # if Esc key is press then break out of the loop

# def video_anlyser(v):
#     print(v)
#     print("f:/project-final/CMPRS/cmprs"+v)
#     input_movie = cv2.VideoCapture(
#         "f:\project-final\CMPRS\cmprs\media\\video_file\WhatsApp_Video_2021-05-25_at_8.34.05_PM_1_8xlcoiV.mp4")
#     print("##########test")
#     print(input_movie)

#     # input_movie = cv2.imdecode(v, cv2.IMREAD_COLOR)
#     while True:
#         (rval, im) = input_movie.read()
#         # cv2.imshow('System',   im)
#         im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
#         mini = cv2.resize(
#             im, (int(im.shape[1] / size), int(im.shape[0] / size)))
#         #faces = classifier.detectMultiScale(mini)
#         face_locations = face_recognition.face_locations(im)
#         # face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#         for face_location in face_locations:
#             # (x, y, w, h) = [v * size for v in f]  #
#             # cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), thickness=4)
#             # sub_face = im[y:y+h, x:x+w]
#             print("######printing subface")
#             # print(sub_face)
#             top, right, bottom, left = face_location
#             face_image = im[top:bottom, left:right]
#             FaceFileName = face_route+"\\face_" + str(y) + ".jpg"
#             cv2.imwrite(FaceFileName, sub_face)
#             f = open(FaceFileName, 'rb')
#             Person.person_image = FaceFileName
#             Person.save()
#         cv2.imshow('System',   im)
#         key = cv2.waitKey(10)
#         # if Esc key is press then break out of the loop
