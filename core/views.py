from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PeopleForm, People2Form

# Create your views here.


def index(request):
    return render(request=request, template_name="home.html")


def fill_step_1(request):

    if request.method == "POST":
        form = PeopleForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/psicologa/2/')

    else:
        form = PeopleForm()

    return render(request, "forms/people.html", {"form": form})


def fill_step_2(request):

    if request.method == "POST":
        form = People2Form(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = People2Form()

    return render(request, "forms/people2.html", {"form": form})
