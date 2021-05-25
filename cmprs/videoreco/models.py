from django.db import models

# Create your models here.


class Video_File(models.Model):
    name = models.CharField(max_length=30)
    video = models.FileField(upload_to="video_file")

    def __str__(self):
        return f"{self.video}"


class Person(models.Model):
    person_image = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True)
    # video_id = models.ForeignKey(
    #     Video_File, on_delete=models.CASCADE
    # )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person_image}"
