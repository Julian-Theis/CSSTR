from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import TestRegistrationForm
# Create your views here.

def home(request):
    return render(request, 'patients/home.html', context={"title" : "Willkommen"})

def registration(request):
    if request.method == 'POST':
        form = TestRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Ein Bestaetigungslink wurde an {email} gesendet. Bitte bestaetigen Sie die Testregistrierung!')
            return redirect('patients-home')

    else:
        form = TestRegistrationForm()
    return render(request, 'patients/registration.html', context={"title" : "Registrierung", "form" : form})

