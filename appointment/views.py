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

def add_schedule(due_date, time, doctor):
    sch = "Day"
    for dt in time[0]+["."]+time[1]:
        if dt == ".":
            sch = "Night"
            continue
        # sch = Schedule.objects.create(
        #     doctor=temp_doc,
        #     schedule=f"{dt}:00-{dt+1}:00 {sch}", 
        #     date=due_date
        # )
        print(due_date, f"{dt}:00-{dt+1}:00 {sch}")


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
            y, m, d = first_date.split('-')
            
            # temp_doc = Doctor.objects.create(email=email)
            temp_doc = ""
            if last_date == "":
                add_schedule(f"{d}-{m}-{y}", rs, temp_doc)
            else:
                y2, m2, d2 = last_date.split('-')
                for rdt in range(int(d), int(d2)+1):
                    add_schedule(f"{rdt}-{m}-{y}", rs, temp_doc)
                    
    return render(request, 'appointment/fill_date_page.html', {})