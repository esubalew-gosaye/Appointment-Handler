from django.db import models

# Create your models here.

class Schedule(models.Model):
    sch = models.CharField(max_length=1200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.sch
    
class Doctor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200, blank=True, null=True)
    speciality = models.CharField(max_length=200, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
