from django.urls import path
from . import views
app_name = 'videoreco'
urlpatterns = [
    path('index/', views.video_uploader_index, name='index'),
    path('create/', views.create_video_uploader,
         name='create_video_uploader'),
    path('detail/<pk>', views.detail_video_anlyser,
         name='detail_video_uploader'),
    path('update/<pk>', views.update_video,
         name='update_video_uploader'),
    path('delete/<pk>', views.delete_video_uploader,
         name='delete_video_uploader'),


]
