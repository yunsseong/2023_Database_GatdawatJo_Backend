# Generated by Django 4.2.7 on 2023-12-05 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0004_patientexamination_diagnosis_prescription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalpersonidentity',
            name='medical_person_detail_address',
        ),
    ]