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
                if not rng in night_schedule:
                    night_schedule.append(rng)
            else:
                if not rng in day_schedule:
                    day_schedule.append(rng)
    return day_schedule, night_schedule
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

            # temp_doc = Doctor.objects.create(email=email)
            
            if last_date == "":
                sch = Schedule.objects.create(day_schedule=rs[0], night_schedule=rs[1], date=first_date)
            else:
                print('else', rs)
            print(first_date, last_date, list_date)

    return render(request, 'appointment/fill_date_page.html', {})