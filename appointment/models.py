from django.db import models


# Create your models here.

class Doctor(models.Model):
    class Meta:
        verbose_name_plural = "Doctors"
        unique_together = ('email', 'phone')

    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200, blank=True, null=True)
    speciality = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.email


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    schedule = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) + " " + self.doctor.email + " " + self.schedule


class Patient(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.email
