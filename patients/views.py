from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import TestRegistrationForm
from .models import Test

import random
import string

def random_string_generator(size=6, chars=string.ascii_uppercase + "123456789"):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_id_generator(instance):
    new_id= random_string_generator()
    Klass= instance.__class__
    qs_exists= Klass.objects.filter(order_id=new_id).exists()
    if qs_exists:
        return unique_id_generator(instance)
    return new_id

# Create your views here.

def home(request):
    return render(request, 'patients/home.html', context={"title" : "Willkommen"})

def registration(request):
    if request.method == 'POST':
        form = TestRegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['code'] = "CODE"

            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Ein Bestaetigungslink wurde an {email} gesendet. Bitte bestaetigen Sie die Testregistrierung!')
            return redirect('patients-home')

    else:
        form = TestRegistrationForm()
    return render(request, 'patients/registration.html', context={"title" : "Registrierung", "form" : form})

