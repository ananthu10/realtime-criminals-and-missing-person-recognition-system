from django.db import models

# Create your models here.


class Recognize(models.Model):
    image = models.FileField(blank=False, null=False)  # file uplaod changed
    location = models.CharField(max_length=100, default='DEFAULT VALUE')
    latitude = models.CharField(max_length=20, default='DEFAULT VALUE')
    longitude = models.CharField(max_length=20, default='DEFAULT VALUE')
    current_time = models.CharField(max_length=20, default='no time bruh!')

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
