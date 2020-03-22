from django.db import models
from django.utils import timezone

class Test(models.Model):
    code = models.CharField(max_length=6, default="")
    email = models.CharField(max_length=100, default="")
    num_people = models.IntegerField(default=1)
    car = models.BooleanField(default=True)
    license_plate = models.CharField(max_length=10, default="")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=timezone.now)

class Patient(models.Model):
    code = models.CharField(max_length=6, default="")
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    birthdate = models.DateField(default=timezone.now)
    zip = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    doctor = models.CharField(max_length=100, default="")
    insurance = models.CharField(max_length=100, default="")
    positive_contact = models.BooleanField(default=True)

    tested = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
