from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import TestRegistrationForm
from .models import Test, Patient
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

def email_verification(request, data):
    test = Test.objects.get(code=data['code'])
    mail_subject = "Corona Test Registrierung - Aktivierung"

    current_site = get_current_site(request)
    message = render_to_string('patients/confirm_email.html', {
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(test.pk)),
        'token': data['code'],
    })

    email = EmailMessage(
        mail_subject, message, to=[data['email']]
    )
    email.send()

def email_code(code, to_email):
    test = Test.objects.get(code=code)
    mail_subject = "Corona Test Registrierung - IHR CODE"
    message = render_to_string('patients/code_email.html', {
        'code': test.code,
    })

    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()


# Create your views here.
def home(request):
    return render(request, 'patients/home.html', context={"title" : "Willkommen"})

def impress(request):
    return render(request, 'patients/impress.html', context={"title" : "Impressum"})

def data(request):
    return render(request, 'patients/data.html', context={"title" : "Datenschutz"})

def registration(request):
    if request.method == 'POST':
        form = TestRegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['code'] = "CODE"
            data = form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Ein Bestaetigungslink wurde an {email} gesendet. Bitte bestaetigen Sie die Testregistrierung!')
            email_verification(request, data)
            return redirect('patients-home')
    else:
        form = TestRegistrationForm()
    return render(request, 'patients/registration.html', context={"title" : "Registrierung", "form" : form})

def activate(request):
    activated = False
    try:
        uidb64 = request.GET['uidb64']
        token = request.GET['token']

        uid = force_text(urlsafe_base64_decode(uidb64))
        test = Test.objects.get(pk=uid)

        patients = Patient.objects.filter(code=token)
        for patient in patients:
            if patient.confirmed is False:
                patient.confirmed = True
                patient.save()
                activated = True

        if activated:
            email_code(token, to_email=test.email)
            return HttpResponse('Ihre Corona Test Registrierung wurde bestätigt. Sie erhalten in Kürze Ihren persönlichen Code per Email, den Sie bitte im CUZ nennen!')
        else:
            return HttpResponse('Registrierung wurde bereits aktiviert.')
    except:
        return HttpResponse('Der Aktivierungslink ist ungültig!')


