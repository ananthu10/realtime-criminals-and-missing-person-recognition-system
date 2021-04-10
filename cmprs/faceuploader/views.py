from django.shortcuts import render, get_object_or_404, redirect
from .models import Face_image
from recognizer.models import Recognize
from .form import ImageForm
from django.http import HttpResponse
# from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView, CreateView
import folium
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from .filters import OrderFilter


@login_required
def face_uploader_index(request):
    print("#########showing rquest##########")
    face_images = Face_image.objects.all()
    print(request.GET)
    myFilter = OrderFilter(request.GET, queryset=face_images)
    print("###################")
    print(myFilter)
    face_images = myFilter.qs
    print("###################")
    print(face_images)
    return render(request, 'faceuploader/main.html',   {
        'face_images': face_images,
        'myFilter': myFilter,
    }
    )


'''def create_face_uploader(request):
     if request.method == 'POST':
         form = ImageForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()
     form = ImageForm()
     img = Face_image.objects.all()
     return render(request, 'faceuploader/create_face_uploader.html', {'img': img, 'form': form})
'''

'''def create_face_uploader(request):
    if request.method == 'POST':
        face_uploader_form = ImageForm(request.POST, request.FILES)
        print(face_uploader_form)
        print("##############")
        print(face_uploader_form.is_valid())
        print("##############")
        if face_uploader_form.is_valid():
            face_uploader_form.save()
            return redirect('faceuploader:index')
    else:
        face_uploader_form = ImageForm()
        return render(request, 'faceuploader/create_face_uploader.html', {
            'face_uploader_form': face_uploader_form
        })
'''
@login_required
def create_face_uploader(request):
    if request.method == 'POST':
        face_uploader_form = ImageForm(request.POST, request.FILES)
        print(face_uploader_form)
        print("##############")
        print(face_uploader_form.is_valid())
        print("##############")
        if face_uploader_form.is_valid():
            face_uploader_form.save()
            return redirect('faceuploader:index')
    else:
        face_uploader_form = ImageForm()
        return render(request, 'faceuploader/create_face_uploader.html', { 'face_uploader_form': face_uploader_form })
@login_required
def detail_face_uploader(request, pk):
    face_image = get_object_or_404(Face_image, pk=pk)
    return render(request, 'faceuploader/detail_face_uploader.html', {'face_image': face_image})

@login_required
def update_face_uploader(request, pk):
    face_image = get_object_or_404(Face_image, pk=pk)
    if request.method == "POST":
        face_uploader_form = ImageForm(request.POST, instance=face_image)
        if face_uploader_form.is_valid():
            face_uploader_form.save()
            return redirect('faceuploader:index')
    else:
        face_uploader_form = ImageForm(instance=face_image)

    return render(
        request, 'faceuploader/create_face_uploader.html',
        {
            'face_uploader_form': face_uploader_form
        }
    )

@login_required
def delete_face_uploader(request, pk):
    face_image = get_object_or_404(Face_image, pk=pk)
    if face_image:
        face_image.delete()
    return redirect('faceuploader:index')

@login_required
def monitor(request):
    reco_face = Recognize.objects.all()
    # for
    # list_reco_face.append(Recognize.objects.get(face_id=pk))
    print(reco_face)
    return render(request, 'faceuploader/monitor.html', {'reco_face': reco_face})

@login_required
def tracker(request, pk):
    # list_reco_face = []
    reco_face = Recognize.objects.filter(face_id=pk)
    print(reco_face)
    if reco_face.count() == 0:
        confirm = True
    else:
        confirm = False
    # for
    # list_reco_face.append(Recognize.objects.get(face_id=pk))

    return render(request, 'faceuploader/tracker.html', {'reco_face': reco_face, 'confirm': confirm})


# def map(request):
#     #map = folium.Map(width=100, height=100, location=[45.5236, -122.6750])
#     map = "hello"
#     # map = map._repr_html_()
#     context = {
#         'map': map
#     }
#     return(request, 'faceuploader/map.html', map)

@login_required
def map(request):
    # reco_face = Recognize.objects.all()
    # for
    # reco_face = folium.Map(width=100, height=100,
    #                        location=[45.5236, -122.6750])
    # reco_face._repr_html_()
    # # list_reco_face.append(Recognize.objects.get(face_id=pk))
    # print(reco_face)
    m = folium.Map([51.5, -0.25], zoom_start=10)
    test = folium.Html('<b>Hello world</b>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    m = m._repr_html_()  # updated
    context = {'reco_face': m}
    print(m)
    return render(request, 'faceuploader/map.html', context)

