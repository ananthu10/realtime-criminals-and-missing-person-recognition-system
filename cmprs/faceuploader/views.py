from django.shortcuts import render, get_object_or_404, redirect
from .models import Face_image
from recognizer.models import Recognize
from .form import ImageForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView, CreateView
import folium

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


# def create_face_uploader(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     form = ImageForm()
#     img = Face_image.objects.all()
#     return render(request, 'faceuploader/create_face_uploader.html', {'img': img, 'form': form})


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
        return render(request, 'faceuploader/create_face_uploader.html', {
            'face_uploader_form': face_uploader_form
        })


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
def map(request, pk):
    # reco_face = Recognize.objects.all()
    # for
    # reco_face = folium.Map(width=100, height=100,
    #                        location=[45.5236, -122.6750])
    # reco_face._repr_html_()
    # # list_reco_face.append(Recognize.objects.get(face_id=pk))
    # print(reco_face)
    map_rec = Recognize.objects.filter(face_id=pk)
    check = False
    m = None
    if map_rec.count() == 0:
        check = True
    else:
        m = folium.Map(
            [map_rec[0].latitude, map_rec[0].longitude], zoom_start=10)
        for map_r in map_rec:
            # str1 = "<b>time:</b>"
            # test = folium.Html('<b>time:</b>', script=True)
            # popup = folium.Popup(test, max_width=2650)
            folium.Marker(
                location=[map_r.latitude, map_r.longitude], popup=f"time:{map_r.image_taken_time}").add_to(m)
            m.add_child(folium.ClickForMarker(
                popup=f"time:{map_r.image_taken_time}"))
        m = m._repr_html_()  # updated
    context = {'reco_face': m, 'check': check}
    # print(m)
    return render(request, 'faceuploader/map.html', context)

    # def index(request):
    #     return render(request, 'index.html',)

    # class FaceUplaodCreateView(CreateView):
    #     model = Face_image
    #     form_class = ImageForm
    #     template_name = 'faceuploader/faceuploder_create.html'

    #     def form_valid(self, form):
    #         form.instance.created_by = self.request.user
    #         return super().form_valid(form)

    # class FaceUplaodDetailView(DetailView):
    #     #context_object_name = 'school_details'
    #     model = Face_image
    #     template_name = 'basic_app/school_detail.html'

    # class FaceUplaodCreateView(CreateView):
    #     fields = ("name", "principal", "location")
    #     model = Face_image

    # class FaceUplaodUpdateView(UpdateView):
    #     fields = ("name", "principal")
    #     model = Face_image

    # class FaceUplaodDeleteView(DeleteView):
    #     model = Face_image
    #     success_url = reverse_lazy("basic_app:list")
