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
        images = []
        encodings = []
        names = []
        files = []
        prsn = Face_image.objects.all()
        for crime in prsn:
            images.append(crime.name+'_image')
            encodings.append(crime.name+'_face_encoding')
            files.append(crime.photo)
            names.append('Name: '+crime.name)
        for i in range(0, len(images)):
            images[i] = face_recognition.load_image_file(files[i])
            encodings[i] = face_recognition.face_encodings(images[i])[0]
        NAME = "Unknown"
        # Create arrays of known face encodings and their names
        known_face_encodings = encodings
        known_face_names = names

        file_serializer = RecognizeSerializer(data=request.data)
        if file_serializer.is_valid():
            image = request.data.get('image')
            location = request.data.get('location')
            latitude = request.data.get('latitude')
            longitude = request.data.get('longitude')
            current_time = request.data.get('current_time')

            # # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)
            # known_face_encoding = [-0.09634063,  0.12095481, -0.00436332, -0.07643753,  0.0080383,
            #                        0.01902981, -0.07184699, -0.09383309,  0.18518871, -0.09588896,
            #                        0.23951106,  0.0986533, -0.22114635, -0.1363683,  0.04405268,
            #                        0.11574756, -0.19899382, -0.09597053, -0.11969153, -0.12277931,
            #                        0.03416885, -0.00267565,  0.09203379,  0.04713435, -0.12731361,
            #                        -0.35371891, -0.0503444, -0.17841317, -0.00310897, -0.09844551,
            #                        -0.06910533, -0.00503746, -0.18466514, -0.09851682,  0.02903969,
            #                        -0.02174894,  0.02261871,  0.0032102,  0.20312519,  0.02999607,
            #                        -0.11646006,  0.09432904,  0.02774341,  0.22102901,  0.26725179,
            #                        0.06896867, -0.00490024, -0.09441824,  0.11115381, -0.22592428,
            #                        0.06230862,  0.16559327,  0.06232892,  0.03458837,  0.09459756,
            #                        -0.18777156,  0.00654241,  0.08582542, -0.13578284,  0.0150229,
            #                        0.00670836, -0.08195844, -0.04346499,  0.03347827,  0.20310158,
            #                        0.09987706, -0.12370517, -0.06683611,  0.12704916, -0.02160804,
            #                        0.00984683,  0.00766284, -0.18980607, -0.19641446, -0.22800779,
            #                        0.09010898,  0.39178532,  0.18818057, -0.20875394,  0.03097027,
            #                        -0.21300618,  0.02532415,  0.07938635,  0.01000703, -0.07719778,
            #                        -0.12651891, -0.04318593,  0.06219772,  0.09163868,  0.05039065,
            #                        -0.04922386,  0.21839413, -0.02394437,  0.06173781,  0.0292527,
            #                        0.06160797, -0.15553983, -0.02440624, -0.17509389, -0.0630486,
            #                        0.01428208, -0.03637431,  0.03971229,  0.13983178, -0.23006812,
            #                        0.04999552,  0.0108454, -0.03970895,  0.02501768,  0.08157793,
            #                        -0.03224047, -0.04502571,  0.0556995, -0.24374914,  0.25514284,
            #                        0.24795187,  0.04060191,  0.17597422,  0.07966681,  0.01920104,
            #                        -0.01194376, -0.02300822, -0.17204897, -0.0596558,  0.05307484,
            #                        0.07417042,  0.07126575,  0.00209804
            #                        ]

            # Load the uploaded image file
            img = face_recognition.load_image_file(image)
            # Get face encodings for any faces in the uploaded image
            unknown_face_encodings = face_recognition.face_encodings(img)

            face_found = False
            is_obama = False

            if len(unknown_face_encodings) > 0:
                face_found = True
                # See if the first face in the uploaded image matches the known face of Obama
                for face_encoding, know_face_name in zip(known_face_encodings, known_face_names):
                    match_results = face_recognition.compare_faces(
                        [face_encoding], unknown_face_encodings[0])
                    if match_results[0]:
                        is_obama = True
                        NAME = know_face_name
            # Return the result as json
            if(is_obama):
                print("face name:"+NAME, "found at "+location)
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
