from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'appointment/index.html', {})

def fill_date(request):
    return render(request, 'appointment/fill_date_page.html', {})