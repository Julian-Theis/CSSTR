from django import forms
from django.contrib.auth.models import User
from .models import Test
from django.contrib.admin.widgets import AdminDateWidget

class TestRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    num_people = forms.IntegerField(min_value=1, max_value=5, label="Anzahl zu testender Personen")
    car = forms.BooleanField(label="Anreise per Auto", required=False)
    license_plate = forms.CharField(max_length=10, label="KfZ-Kennzeichen", required=False)

    firstname = forms.CharField(max_length=100, label="Vorname")
    lastname = forms.CharField(max_length=100, label="Nachname")
    birth_date = forms.DateField(widget=AdminDateWidget, label="Geburtsdatum")
    zip = forms.CharField(max_length=5, label="PLZ")
    city = forms.CharField(max_length=100, label="Ort")
    phone = forms.CharField(max_length=100, label="Telefon")
    doctor = forms.CharField(max_length=100, label="Hausarzt")
    insurance = forms.CharField(max_length=100, label="Krankenkasse")
    positive_contact = forms.BooleanField(label="Kontakt zu positiver COVID-19 Person?", required=False)

    security = forms.BooleanField(label="Ich bin mit der Datenschutzerklaerung einverstanden")

    class Meta:
        model = Test
        fields = ['email',
                  'num_people',
                  'car',
                  'license_plate',
                  'firstname',
                  'lastname',
                  'birth_date',
                  'zip',
                  'city',
                  'phone',
                  'doctor',
                  'insurance',
                  'positive_contact',
                  'security'
                  ]