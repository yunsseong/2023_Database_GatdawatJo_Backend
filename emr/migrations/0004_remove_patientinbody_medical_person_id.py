# Generated by Django 4.2.7 on 2023-12-16 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0003_remove_patientinbody_ecw_ratio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinbody',
            name='medical_person_id',
        ),
    ]
