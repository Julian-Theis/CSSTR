from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from patients.models import Test

# Create your views here.

def archive(archive_id):
    test = Test.objects.get(pk=archive_id)
    test.tested = True
    test.save()


@login_required(login_url="staff-login")
def home(request):
    if request.method == 'GET':
        try:
            form = SearchForm(request.GET)
            code = form.data['code']
            tests = Test.objects.filter(code=code, tested=False)
        except:
            code = None
            tests = []
    else:
        form = SearchForm()
        code = None
        tests = []

    if request.method == 'GET' and 'id' in request.GET.keys():
        id = request.GET['id']
    else:
        id = -1

    if request.method == 'GET' and 'archive' in request.GET.keys():
        archive_id = request.GET['archive']
        archive(archive_id)

    total_reg = len(Test.objects.all())
    open_reg = len(Test.objects.filter(tested=False))
    open_test = len(Test.objects.filter(tested=True))

    context = {
        "title": "Mitarbeiter",
        "form": form,
        "code": code,
        "tests":tests,
        "id" : int(id),
        "total_reg" : total_reg,
        "open_reg" : open_reg,
        "open_test" : open_test
    }
    return render(request, 'staff/home.html', context=context)