from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecognizeSerializer
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# from forms import EmployeeForm
# Create your views here.
import face_recognition
from faceuploader.models import Face_image
import numpy as np


class RecognizeUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        #############################################
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

        file_serializer = RecognizeSerializer(data=request.data)

        if file_serializer.is_valid():
            image = request.data.get('image')
            location = request.data.get('location')
            latitude = request.data.get('latitude')
            longitude = request.data.get('longitude')
            image_taken_time = request.data.get('image_taken_time')
            print(location, latitude)
            print(image)
            img = face_recognition.load_image_file(image)

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
                print("face name:"+NAME, "found at " +
                      location + "face id "+str(find_id))
                file_serializer.save(face_id=find_id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.parsers import FileUploadParser
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import RecognizeSerializer
# from rest_framework import status
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy
# from django.views.generic import TemplateView
# # from forms import EmployeeForm
# # Create your views here.
# import face_recognition
# from faceuploader.models import Face_image
# import numpy as np


# class RecognizeUploadView(APIView):
#     parser_class = (FileUploadParser,)

#     def post(self, request, *args, **kwargs):
#         #############################################
#         images = []
#         encodings = []
#         names = []
#         files = []
#         ids = []
#         prsn = Face_image.objects.all()
#         for crime in prsn:
#             images.append(crime.name+'_image')
#             encodings.append(crime.name+'_face_encoding')
#             files.append(crime.photo)
#             ids.append(crime.id)
#             names.append('Name: '+crime.name)
#         for i in range(0, len(images)):
#             images[i] = face_recognition.load_image_file(files[i])
#             encodings[i] = face_recognition.face_encodings(images[i])[0]
#             print("####################")
#             print(type(encodings))
#             print("####################")
#         NAME = "Unknown"
#         known_face_encodings = encodings

#         known_face_names = names

#         file_serializer = RecognizeSerializer(data=request.data)

#         if file_serializer.is_valid():
#             image = request.data.get('image')
#             location = request.data.get('location')
#             latitude = request.data.get('latitude')
#             longitude = request.data.get('longitude')
#             image_taken_time = request.data.get('image_taken_time')
#             print(location, latitude)
#             print(image)
#             img = face_recognition.load_image_file(image)

#             unknown_face_encodings = face_recognition.face_encodings(img)
#             face_found = False
#             is_obama = False
#             if len(unknown_face_encodings) > 0:
#                 face_found = True

#                 for face_encoding, know_face_name, ij in zip(known_face_encodings, known_face_names, prsn):
#                     match_results = face_recognition.compare_faces(
#                         [face_encoding], unknown_face_encodings[0])
#                     if match_results[0]:
#                         is_obama = True
#                         NAME = know_face_name
#                         find_id = ij

#             if(is_obama):
#                 print("face name:"+NAME, "found at " +
#                       location + "face id "+str(find_id))
#                 file_serializer.save(face_id=find_id)
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeImage(TemplateView):
#     form = EmployeeForm
#     template_name = 'emp_image.html'

#     def post(self, request, *args, **kwargs):
#         form = EmployeeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
#         context = self.get_context_data(form=form)
#         return self.render_to_response(context)

#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
# @api_view(['POST'])
# def recognize(request):
#     #  serializer = TaskSerializer(data=request.data)

#     #  if serializer.is_valid():
#     #      serializer.save()
#     data = request.data

#     return Response(serializer.data)


# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)
