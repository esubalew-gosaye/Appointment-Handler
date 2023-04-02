from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
# Create your views here.
def date_spliter(date_list, spliter=60):
    night_schedule = []
    day_schedule = []

    for elm in date_list.split(','):
        st, end, t = elm.split(':')
        # TODO: add validation for time or pop up error
        for rng in range(int(st), int(end)):
            if t == 'n' or t == 'N':
                if not rng in night_schedule:
                    night_schedule.append(rng)
            else:
                if not rng in day_schedule:
                    day_schedule.append(rng)
    return day_schedule, night_schedule

def add_schedule(due_date, time, doctor):
    sch = "Day"
    for dt in time[0]+["."]+time[1]:
        if dt == ".":
            sch = "Night"
            continue
        Schedule.objects.create(
            doctor=doctor,
            schedule=f"{dt}:00-{dt+1}:00 {sch}", 
            date=due_date
        )


def index(request):
    unique_dates = []
    list_schedlue = []
    if request.method == 'POST':
        if request.POST.get('list_schedule'):
            doctor = request.POST.get('doctor')
            date = request.POST.get('sp_date')

            list_schedlue = Schedule.objects.filter(doctor=doctor)
            if date != "":
                list_schedlue = list_schedlue.filter(date=date)
            for sch in list_schedlue:
                if not sch.date in unique_dates:
                    unique_dates.append(sch.date)

            print(unique_dates, list_schedlue)
    context = {
        'dates': unique_dates,
        'schedules': list_schedlue,
        'doctors': Doctor.objects.all(),
    }
    return render(request, 'appointment/index.html', context)

def fill_date(request):
    if request.method == 'POST':
        if request.POST.get('fill_date'):
            email = request.POST.get('email')
            first_date = request.POST.get('date-first')
            last_date = request.POST.get('date-final')
            list_date = request.POST.get('date-input')

            rs = date_spliter(list_date)
            y, m, d = first_date.split('-')
            
            temp_doc = Doctor.objects.create(email=email)

            if last_date == "":
                add_schedule(f"{y}-{m}-{d}", rs, temp_doc)
            else:
                y2, m2, d2 = last_date.split('-')
                for rdt in range(int(d), int(d2)+1):
                    add_schedule(f"{y}-{m}-{rdt}", rs, temp_doc)
                    
    return render(request, 'appointment/fill_date_page.html', {})