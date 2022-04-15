from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')




def feinstaub(request):
    return render(request, 'feinstaub.html')

def landnutzung(request):
    return render(request, 'landnutzung.html')

def analyse_10_10_2019(request):
    return render(request, 'analyse_10_10_2019.html')


def leute(request):
    return render(request, 'leute.html')

def kontakt(request):
    return render(request, 'kontakt.html')




def test_page(request):
    return render(request, 'test_page.html')

def test_page2(request):
    return render(request, 'test_page.html')
