from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from patients.models import Test, Patient

def archive(archive_id):
    patient = Patient.objects.get(pk=archive_id)
    patient.tested = True
    patient.save()

@login_required(login_url="staff-login")
def home(request):
    if request.method == 'GET':
        try:
            form = SearchForm(request.GET)
            code = form.data['code']
            patients = Patient.objects.filter(code=code, tested=False)
            print(patients)
        except:
            code = None
            patients = []

    else:
        form = SearchForm()
        code = None
        patients = []

    if request.method == 'GET' and 'id' in request.GET.keys():
        id = request.GET['id']
    else:
        id = -1

    if request.method == 'GET' and 'archive' in request.GET.keys():
        archive_id = request.GET['archive']
        archive(archive_id)

    for patient in patients:
        t = Test.objects.get(code=patient.code)
        patient.email = t.email
        patient.num_people = t.num_people
        patient.car = t.car
        patient.license_plate = t.license_plate
        patient.date_created = t.date_created
        patient.last_modified = t.last_modified

    total_reg = len(Patient.objects.all())
    open_reg = len(Patient.objects.filter(tested=False))
    open_test = len(Patient.objects.filter(tested=True))

    context = {
        "title": "Mitarbeiter",
        "form": form,
        "code": code,
        "tests": patients,
        "id" : int(id),
        "total_reg" : total_reg,
        "open_reg" : open_reg,
        "open_test" : open_test
    }
    return render(request, 'staff/home.html', context=context)