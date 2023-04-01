from django.db import models

# Create your models here.

class Schedule(models.Model):
    doctor = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctor.name + ' ' + self.date + ' ' + self.time
    
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, required=True)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    schedule = models.ManyToOneRel(Schedule, blank=True)

    def __str__(self):
        return self.name
    
