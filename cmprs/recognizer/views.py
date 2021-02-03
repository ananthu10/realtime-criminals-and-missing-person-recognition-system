from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecognizeSerializer
from rest_framework import status
# Create your views here.


class RecognizeUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = RecognizeSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
