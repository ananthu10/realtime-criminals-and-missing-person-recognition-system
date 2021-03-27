from django.db import models

# Create your models here.


class Face_image(models.Model):
    photo = models.ImageField(upload_to="train_image")
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    # OVERIDE TO RETURN VALUE
