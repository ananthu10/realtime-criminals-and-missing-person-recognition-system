from django.shortcuts import render, get_object_or_404, redirect
from .models import Face_image
from recognizer.models import Recognize
from .form import ImageForm
from django.http import HttpResponse
# from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView, CreateView


def face_uploader_index(request):
    face_images = Face_image.objects.all()
    return render(request, 'faceuploader/main.html',   {
        'face_images': face_images
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


def detail_face_uploader(request, pk):
    face_image = get_object_or_404(Face_image, pk=pk)
    return render(request, 'faceuploader/detail_face_uploader.html', {'face_image': face_image})


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


def delete_face_uploader(request, pk):
    face_image = get_object_or_404(Face_image, pk=pk)
    if face_image:
        face_image.delete()
    return redirect('faceuploader:index')


def monitor(request):
    reco_face = Recognize.objects.all()
    # for
    # list_reco_face.append(Recognize.objects.get(face_id=pk))
    print(reco_face)
    return render(request, 'faceuploader/monitor.html', {'reco_face': reco_face})


def tracker(request, pk):
    #list_reco_face = []
    reco_face = Recognize.objects.filter(face_id=pk)
    # for
    # list_reco_face.append(Recognize.objects.get(face_id=pk))
    print(reco_face)
    return render(request, 'faceuploader/tracker.html', {'reco_face': reco_face})
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
