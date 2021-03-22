from django.db import models

# Create your models here.


class Recognize(models.Model):
    image = models.FileField(blank=False, null=False)  # file uplaod changed

    def __str__(self):
        return self.image.name
    # def save(self, *args, **kwargs):
    #     detected_img = Image.fromarray(orig)
    #     buffer = BytesIO()
    #     detected_img.save(buffer, format='png')
    #     image_png = buffer.getvalue()
    #     self.file1.save(str(self.file1), ContentFile(image_png), save=False)
    #     super().save(*args, **kwargs)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')
