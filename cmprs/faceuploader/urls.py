from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),


]


# from django.contrib import admin
# from django.urls import include, path
# urlpatterns = [
# path(‘homepage/’, include(‘app.urls’)),
# path(‘admin/’, admin.site.urls),
# ]
