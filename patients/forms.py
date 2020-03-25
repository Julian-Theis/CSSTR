from django import forms
from django.contrib.auth.models import User
from .models import Test
from .models import Patient
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import HiddenInput
from patients.utils import unique_id_generator
import datetime

class TestRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    num_people = forms.IntegerField(min_value=1, max_value=5, label="Anzahl zu testender Personen",initial=1)
    car = forms.BooleanField(label="Kommen Sie mit dem Auto?", required=False)
    license_plate = forms.CharField(max_length=10, label="KfZ-Kennzeichen", required=False)
    privacy = forms.BooleanField(label="Ich bin mit der Datenschutzerklaerung einverstanden")

    firstname = forms.CharField(max_length=100, label="Vorname")
    lastname = forms.CharField(max_length=100, label="Nachname")
    birth_date = forms.DateField(widget=AdminDateWidget, label="Geburtsdatum")
    streetaddress = forms.CharField(max_length=5, label="Strasse und Hausnummer")
    zip = forms.CharField(max_length=5, label="PLZ")
    city = forms.CharField(max_length=100, label="Ort")
    phone = forms.CharField(max_length=100, label="Telefon")
    doctor = forms.CharField(max_length=100, label="Hausarzt")
    doctor_city = forms.CharField(max_length=100, label="Ort des Hausarztes")
    insurance = forms.CharField(max_length=100, label="Krankenkasse")
    positive_contact = forms.BooleanField(label="Kontakt zu einer mit dem Coronavirus infizierten Person?", required=False)

    firstname_2 = forms.CharField(max_length=100, label="Vorname", required=False)
    lastname_2 = forms.CharField(max_length=100, label="Nachname", required=False)
    birth_date_2 = forms.DateField(widget=AdminDateWidget, label="Geburtsdatum", required=False)
    streetaddress_2 = forms.CharField(max_length=5, label="Strasse und Hausnummer", required=False)
    zip_2 = forms.CharField(max_length=5, label="PLZ", required=False)
    city_2 = forms.CharField(max_length=100, label="Ort", required=False)
    phone_2 = forms.CharField(max_length=100, label="Telefon", required=False)
    doctor_2 = forms.CharField(max_length=100, label="Hausarzt", required=False)
    doctor_city_2 = forms.CharField(max_length=100, label="Ort des Hausarztes", required=False)
    insurance_2 = forms.CharField(max_length=100, label="Krankenkasse", required=False)
    positive_contact_2 = forms.BooleanField(label="Kontakt zu einer mit dem Coronavirus infizierten Person?", required=False)

    firstname_3 = forms.CharField(max_length=100, label="Vorname", required=False)
    lastname_3 = forms.CharField(max_length=100, label="Nachname", required=False)
    birth_date_3 = forms.DateField(widget=AdminDateWidget, label="Geburtsdatum", required=False)
    streetaddress_3 = forms.CharField(max_length=5, label="Strasse und Hausnummer", required=False)
    zip_3 = forms.CharField(max_length=5, label="PLZ", required=False)
    city_3 = forms.CharField(max_length=100, label="Ort", required=False)
    phone_3 = forms.CharField(max_length=100, label="Telefon", required=False)
    doctor_3 = forms.CharField(max_length=100, label="Hausarzt", required=False)
    doctor_city_3 = forms.CharField(max_length=100, label="Ort des Hausarztes", required=False)
    insurance_3 = forms.CharField(max_length=100, label="Krankenkasse", required=False)
    positive_contact_3 = forms.BooleanField(label="Kontakt zu einer mit dem Coronavirus infizierten Person?", required=False)

    firstname_4 = forms.CharField(max_length=100, label="Vorname", required=False)
    lastname_4 = forms.CharField(max_length=100, label="Nachname", required=False)
    birth_date_4 = forms.DateField(widget=AdminDateWidget, label="Geburtsdatum", required=False)
    streetaddress_4 = forms.CharField(max_length=5, label="Strasse und Hausnummer", required=False)
    zip_4 = forms.CharField(max_length=5, label="PLZ", required=False)
    city_4 = forms.CharField(max_length=100, label="Ort", required=False)
    phone_4 = forms.CharField(max_length=100, label="Telefon", required=False)
    doctor_4 = forms.CharField(max_length=100, label="Hausarzt", required=False)
    doctor_city_4 = forms.CharField(max_length=100, label="Ort des Hausarztes", required=False)
    insurance_4 = forms.CharField(max_length=100, label="Krankenkasse", required=False)
    positive_contact_4 = forms.BooleanField(label="Kontakt zu einer mit dem Coronavirus infizierten Person?", required=False)

    firstname_5 = forms.CharField(max_length=100, label="Vorname", required=False)
    lastname_5 = forms.CharField(max_length=100, label="Nachname", required=False)
    birth_date_5 = forms.DateField(widget=AdminDateWidget, label="Geburtsdatum", required=False)
    streetaddress_5 = forms.CharField(max_length=5, label="Strasse und Hausnummer", required=False)
    zip_5 = forms.CharField(max_length=5, label="PLZ", required=False)
    city_5 = forms.CharField(max_length=100, label="Ort", required=False)
    phone_5 = forms.CharField(max_length=100, label="Telefon", required=False)
    doctor_5 = forms.CharField(max_length=100, label="Hausarzt", required=False)
    doctor_city_5 = forms.CharField(max_length=100, label="Ort des Hausarztes", required=False)
    insurance_5 = forms.CharField(max_length=100, label="Krankenkasse", required=False)
    positive_contact_5 = forms.BooleanField(label="Kontakt zu einer mit dem Coronavirus infizierten Person?", required=False)

    class Meta:
        model = Test
        fields = ['email',
                  'num_people',
                  'car',
                  'license_plate',
                  'firstname',
                  'lastname',
                  'birth_date',
                  'streetaddress',
                  'zip',
                  'city',
                  'phone',
                  'doctor',
                  'doctor_city',
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
        test.car = self.cleaned_data["car"]
        test.license_plate = self.cleaned_data["license_plate"]
        test.save()
        Patient.objects.create(
            code=test.code,
            firstname=self.cleaned_data["firstname"],
            lastname=self.cleaned_data["lastname"],
            birthdate=self.cleaned_data["birth_date"],
            streetaddress=self.cleaned_data["streetaddress"],
            zip=self.cleaned_data["zip"],
            city=self.cleaned_data["city"],
            phone=self.cleaned_data["phone"],
            doctor=self.cleaned_data["doctor"],
            doctor_city = self.cleaned_data["doctor_city"],
            insurance=self.cleaned_data["insurance"],
            positive_contact=self.cleaned_data["positive_contact"]
        )
        if self.cleaned_data["num_people"] > 1:
            Patient.objects.create(
                code=test.code,
                firstname=self.cleaned_data["firstname_2"],
                lastname=self.cleaned_data["lastname_2"],
                birthdate=self.cleaned_data["birth_date_2"],
                streetaddress=self.cleaned_data["streetaddress_2"],
                zip=self.cleaned_data["zip_2"],
                city=self.cleaned_data["city_2"],
                phone=self.cleaned_data["phone_2"],
                doctor=self.cleaned_data["doctor_2"],
                doctor_city=self.cleaned_data["doctor_city_2"],
                insurance=self.cleaned_data["insurance_2"],
                positive_contact=self.cleaned_data["positive_contact_2"]
            )
        if self.cleaned_data["num_people"] > 2:
            Patient.objects.create(
                code=test.code,
                firstname=self.cleaned_data["firstname_3"],
                lastname=self.cleaned_data["lastname_3"],
                birthdate=self.cleaned_data["birth_date_3"],
                streetaddress=self.cleaned_data["streetaddress_3"],
                zip=self.cleaned_data["zip_3"],
                city=self.cleaned_data["city_3"],
                phone=self.cleaned_data["phone_3"],
                doctor=self.cleaned_data["doctor_3"],
                doctor_city=self.cleaned_data["doctor_city_3"],
                insurance=self.cleaned_data["insurance_3"],
                positive_contact=self.cleaned_data["positive_contact_3"]
            )
        if self.cleaned_data["num_people"] > 3:
            Patient.objects.create(
                code=test.code,
                firstname=self.cleaned_data["firstname_4"],
                lastname=self.cleaned_data["lastname_4"],
                birthdate=self.cleaned_data["birth_date_4"],
                streetaddress=self.cleaned_data["streetaddress_4"],
                zip=self.cleaned_data["zip_4"],
                city=self.cleaned_data["city_4"],
                phone=self.cleaned_data["phone_4"],
                doctor=self.cleaned_data["doctor_4"],
                doctor_city=self.cleaned_data["doctor_city_4"],
                insurance=self.cleaned_data["insurance_4"],
                positive_contact=self.cleaned_data["positive_contact_4"]
            )
        if self.cleaned_data["num_people"] > 4:
            Patient.objects.create(
                code=test.code,
                firstname=self.cleaned_data["firstname_5"],
                lastname=self.cleaned_data["lastname_5"],
                birthdate=self.cleaned_data["birth_date_5"],
                streetaddress=self.cleaned_data["streetaddress_5"],
                zip=self.cleaned_data["zip_5"],
                city=self.cleaned_data["city_5"],
                phone=self.cleaned_data["phone_5"],
                doctor=self.cleaned_data["doctor_5"],
                doctor_city=self.cleaned_data["doctor_city_5"],
                insurance=self.cleaned_data["insurance_5"],
                positive_contact=self.cleaned_data["positive_contact_5"]
            )
        return {"email" : test.email, "code" : test.code}
