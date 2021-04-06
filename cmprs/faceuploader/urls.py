from django.urls import path
from . import views
app_name = 'faceuploader'
urlpatterns = [
    path('', views.monitor, name='monitor'),
    path('index/', views.face_uploader_index, name='index'),
    path('create/', views.create_face_uploader,
         name='create_face_uploader'),
    path('detail/<pk>', views.detail_face_uploader,
         name='detail_face_uploader'),
    path('update/<pk>', views.update_face_uploader,
         name='update_face_uploader'),
    path('delete/<pk>', views.delete_face_uploader,
         name='delete_face_uploader'),
    path('track/<pk>', views.tracker,
         name='track'),
    path('map/', views.map,
         name='map'),


]


# from django.contrib import admin
# from django.urls import include, path
# urlpatterns = [
# path(‘homepage/’, include(‘app.urls’)),
# path(‘admin/’, admin.site.urls),
# ]
