from django.db import models

# Create your models here.

from faceuploader.models import Face_image


class Recognize(models.Model):

    #image = models.ImageField(blank=False, null=False)
    image = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True)
    location = models.CharField(max_length=100, default='DEFAULT VALUE')
    latitude = models.CharField(max_length=20, default='DEFAULT VALUE')
    longitude = models.CharField(max_length=20, default='DEFAULT VALUE')
    current_time = models.CharField(max_length=20, default='no time bruh!')
    face_id = models.ForeignKey(
        Face_image, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.image.name
    # def save(self, *args, **kwargs):
    #     detected_img = Image.fromarray(orig)
    #     buffer = BytesIO()
    #     detected_img.save(buffer, format='png')
    #     image_png = buffer.getvalue()
    #     self.file1.save(str(self.file1), ContentFile(image_png), save=False)
    #     super().save(*args, **kwargs)


# class Employee(models.Model):
#     name = models.CharField(max_length=50)
#     emp_image = models.ImageField(upload_to='upload/')
