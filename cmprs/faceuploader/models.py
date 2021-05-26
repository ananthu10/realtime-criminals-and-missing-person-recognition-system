from django.db import models
import datetime
# Create your models here.
from django.utils.timezone import now


class Face_image(models.Model):
    FCHOICES = (
        ('MISSING', 'Missing'),
        ('CRIMINAL', 'Criminal'),
    )
    photo = models.ImageField(upload_to="train_image")
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    dob = models.DateField()
    GCHOICES = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )
    gender = models.CharField(choices=GCHOICES, max_length=20, default='none')
    case = models.CharField(choices=FCHOICES, max_length=20, default='Missing')
    address = models.CharField(max_length=200, default='')
    missing_date = models.DateTimeField(default=now, blank=True)
    incident_location = models.CharField(max_length=200, default='')

    description = models.TextField(max_length=200, default='no data')

    def __str__(self):
        return f"{self.id}"

    # def __str__(self):
    #     return f"{self.name}-{self.id}"
