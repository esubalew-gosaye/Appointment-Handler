from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def date_spliter(date_list, spliter=60):
    night_schedule = []
    day_schedule = []

    for elm in date_list.split(','):
        st, end, t = elm.split(':')
        for rng in range(int(st), int(end)):
            if t == 'n' or t == 'N':
                night_schedule.append(rng)
            else:
                day_schedule.append(rng)
    return night_schedule, day_schedule
def index(request):
    return render(request, 'appointment/index.html', {})

def fill_date(request):
    if request.method == 'POST':
        if request.POST.get('fill_date'):
            email = request.POST.get('email')
            first_date = request.POST.get('date-first')
            last_date = request.POST.get('date-final')
            list_date = request.POST.get('date-input')
            rs = date_spliter(list_date)
            print(rs, list_date, first_date, last_date, email)

    return render(request, 'appointment/fill_date_page.html', {})