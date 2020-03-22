from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from patients.models import Test

class SearchForm(forms.Form):
    code = forms.CharField(max_length=6, required=False)

    class Meta:
        model = Test
        fields = ['code']