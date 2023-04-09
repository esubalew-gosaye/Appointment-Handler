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
    for dt in time[0] + ["."] + time[1]:
        if dt == ".":
            sch = "Night"
            continue
        Schedule.objects.create(
            doctor=doctor,
            schedule=f"{dt}:00-{dt + 1}:00 {sch}",
            date=due_date
        )


# TODO Change the time format to gregorian when user selects

def index(request):
    unique_dates = []
    list_schedule = []
    get_values = []
    if request.method == 'GET':
        if request.GET.get('list_schedule'):
            doctor = request.GET.get('doctor')
            date = request.GET.get('sp_date')
            list_schedule = Schedule.objects.filter(doctor=doctor).filter(is_booked=False)
            if date != "":
                list_schedule = list_schedule.filter(date=date)
            for sch in list_schedule:
                if not sch.date in unique_dates:
                    unique_dates.append(sch.date)
    if request.method == "POST":
        if request.POST.get('login'):
            email = request.POST.get('email')
            pt = Patient.objects.filter(email=email)
            if pt.exists():
                usr = pt[0]
                request.session['user-name'] = usr.name
                request.session['user-email'] = usr.email

        # finally executed under GET method to deliver all values to the fronted
        get_values = {itm: val for itm, val in request.GET.items()}

    # calapi = calendarific.v2('268618031bd278a6222a52c2b261181a5868d6c3')
    #
    # parameters = {
    #     'country': 'ET',
    #     'year': 2019,
    # }
    #
    # holidays = calapi.holidays(parameters)
    # print(holidays)

    context = {
        'login-status': {"email": request.session['user-email']},
        'dates': sorted(unique_dates)[:6],
        'schedules': list_schedule,
        'get': get_values,
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

            temp_doc, created = Doctor.objects.get_or_create(email=email)

            if last_date == "":
                add_schedule(f"{y}-{m}-{d}", rs, temp_doc)
            else:
                y2, m2, d2 = last_date.split('-')
                for rdt in range(int(d), int(d2) + 1):
                    add_schedule(f"{y}-{m}-{rdt}", rs, temp_doc)

    return render(request, 'appointment/fill_date_page.html', {})
