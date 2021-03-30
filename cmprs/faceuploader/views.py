from django.shortcuts import render
from .models import Face_image
from .form import ImageForm
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html',)


def faceupload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Face_image.objects.all()
    return render(request, 'faceupload/home.html', {'img': img, 'form': form})
