from django import forms
from django.contrib.auth.models import User
from .models import Test
from .models import Patient
from django.contrib.admin.widgets import AdminDateWidget
from patients.utils import unique_id_generator
import datetime

class TestRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    num_people = forms.IntegerField(min_value=1, max_value=5, label="Anzahl zu testender Personen",initial=1)
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
    positive_contact = forms.BooleanField(label="Kontakt zu einer mit dem Coronavirus infizierten Person?", required=False)
    car = forms.BooleanField(label="Kommen Sie mit dem Auto?", required=False)
    privacy = forms.BooleanField(label="Ich bin mit der Datenschutzerklaerung einverstanden")

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
                  'privacy',
                  'car'
                  ]

    def save(self,*args, **kwargs):
        test = self.instance
        test.email = self.cleaned_data["email"]
        test.code = unique_id_generator()
        test.num_people = self.cleaned_data["num_people"]
        test.car = self.cleaned_data["num_people"]
        #test.license_plate =
        test.save()
        Patient.objects.create(
            code=test.code,
            firstname=self.cleaned_data["firstname"],
            lastname=self.cleaned_data["lastname"],
            birthdate=self.cleaned_data["birth_date"],
            zip=self.cleaned_data["zip"],
            city=self.cleaned_data["city"],
            phone=self.cleaned_data["phone"],
            doctor=self.cleaned_data["doctor"],
            insurance=self.cleaned_data["insurance"],
            positive_contact=self.cleaned_data["positive_contact"]
        )
        return {"email" : test.email, "code" : test.code}