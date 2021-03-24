from django.shortcuts import render
from .models import image
from .form import ImageForm
# Create your views here.


def faceupload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = image.objects.all()
    return render(request, 'faceupload/home.html', {'img': img, 'form': form})