from django.shortcuts import render
from .models import Person, Passport, Reporter, Article, Fuel, Car


def person_list(request):
    people = Person.objects.all()
    return render(request, 'mvt/people.html', {'person_list': people})


def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    return render(request, 'mvt/person_detail.html', {'person': person})


def passport_list(request):
    passport = Passport.objects.all()
    return render(request, 'mvt/passport.html', {'passport_list': passport})


def passport_detail(request, pk):
    passport_number = Passport.objects.get(pk=pk)
    return render(request, 'mvt/passport_detail.html', {'passport_number': passport_number})


def reporter_list(request):
    reporter = Reporter.objects.all()
    return render(request, 'mvt/reporter_list.html', {'reporter_list': reporter})


def reporter_detail(request, pk):
    reporter = Reporter.objects.get(pk=pk)
    return render(request, 'mvt/reporter_detail.html', {'reporter': reporter})


def article_list(request):
    article = Article.objects.all()
    return render(request, 'mvt/article_list.html', {'article_list': article})


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'mvt/article_detail.html', {'article': article})


def fuel_list(request):
    fuel = Fuel.objects.all()
    return render(request, 'mvt/fuel_list.html', {'fuel_list': fuel})


def fuel_detail(request, pk):
    fuel = Fuel.objects.get(pk=pk)
    return render(request, 'mvt/fuel_detail.html', {'fuel': fuel})


def car_list(request):
    name = Car.objects.all()
    return render(request, 'mvt/car_list.html', {'car_list': name})


def car_detail(request, pk):
    name = Car.objects.get(pk=pk)
    return render(request, 'mvt/car_detail.html', {'car': name})



def mvt(request):
    if request.method == 'GET':
        return render(request, 'mvt/mvt.html')
