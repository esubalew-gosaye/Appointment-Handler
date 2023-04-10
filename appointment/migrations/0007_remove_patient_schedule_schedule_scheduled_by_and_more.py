# Generated by Django 4.1.7 on 2023-04-10 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='schedule',
        ),
        migrations.AddField(
            model_name='schedule',
            name='scheduled_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.patient'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.doctor'),
        ),
    ]
