# Generated by Django 4.2.7 on 2023-12-16 08:45

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('chart_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('diagnosis', models.TextField(default='')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('image_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image_url', models.ImageField(upload_to='uploaded_pictures')),
            ],
            options={
                'db_table': 'chart',
            },
        ),
        migrations.CreateModel(
            name='ClassificationCode',
            fields=[
                ('classification_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('classification_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_code', models.CharField(max_length=50, unique=True)),
                ('disease_name', models.CharField(max_length=200)),
                ('disease_description', models.TextField()),
            ],
            options={
                'db_table': 'disease',
            },
        ),
        migrations.CreateModel(
            name='InspectType',
            fields=[
                ('inspect_type_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('inspect_type', models.CharField(max_length=50, verbose_name='검사 종류')),
                ('inspect_cost', models.IntegerField()),
            ],
            options={
                'db_table': 'inspect_type',
            },
        ),
        migrations.CreateModel(
            name='MedicalPersonIdentity',
            fields=[
                ('medical_person_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('medical_person_name', models.CharField(max_length=60)),
                ('medical_person_system_id', models.CharField(max_length=20)),
                ('medical_person_gender', models.CharField(max_length=2)),
                ('medical_person_birthday', models.DateField()),
                ('medical_person_phone_number', models.CharField(max_length=15)),
                ('medical_person_main_address', models.TextField()),
                ('medical_person_license', models.TextField()),
                ('classification_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.classificationcode')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emr.customuser')),
            ],
            options={
                'db_table': 'medical_person_identity',
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('medication_code', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('medication_name', models.CharField(max_length=200)),
                ('medication_type', models.CharField(max_length=100)),
                ('medication_description', models.TextField()),
                ('administration_method', models.TextField()),
                ('medication_cost', models.IntegerField()),
            ],
            options={
                'db_table': 'medication',
            },
        ),
        migrations.CreateModel(
            name='PatientIdentity',
            fields=[
                ('patient_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=60)),
                ('patient_gender', models.CharField(max_length=1)),
                ('patient_birth', models.CharField(max_length=8)),
                ('patient_residence_number', models.CharField(max_length=8)),
                ('patient_phone_number', models.CharField(max_length=15)),
                ('patient_emergency_phone_number', models.CharField(max_length=15)),
                ('patient_address', models.CharField(max_length=100)),
                ('patient_agree_essential_term', models.BooleanField(default=False)),
                ('patient_agree_optional_term', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'patient_identity',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('treatment_code', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('treatment_name', models.CharField(max_length=200)),
                ('treatment_cost', models.IntegerField()),
            ],
            options={
                'db_table': 'treatment',
            },
        ),
        migrations.CreateModel(
            name='XRay',
            fields=[
                ('xray_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shooting_timestamp', models.DateTimeField()),
                ('original_xray_location', models.BinaryField()),
                ('medical_person_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.medicalpersonidentity')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'xray',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('reception_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('visit_reason', models.TextField()),
                ('reception_date', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='emr.patientidentity')),
            ],
            options={
                'db_table': 'reception',
            },
        ),
        migrations.CreateModel(
            name='PatientList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'patient_list',
            },
        ),
        migrations.CreateModel(
            name='Inspect',
            fields=[
                ('inspect_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('inspect_date', models.DateTimeField(auto_now=True)),
                ('inspect_content', models.TextField(verbose_name='검사 내용')),
                ('inspect_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.inspecttype')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'inspect',
            },
        ),
        migrations.CreateModel(
            name='Inbody',
            fields=[
                ('inbody_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weight', models.FloatField()),
                ('muscle_mass', models.FloatField()),
                ('body_fat_mass', models.FloatField()),
                ('bmi', models.FloatField()),
                ('percent_body_fat', models.FloatField()),
                ('right_arm', models.FloatField()),
                ('left_arm', models.FloatField()),
                ('trunk', models.FloatField()),
                ('right_leg', models.FloatField()),
                ('left_leg', models.FloatField()),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('original_file_location', models.BinaryField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'inbody',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image_title', models.TextField(default='a.jpg', null=True)),
                ('image_url', models.ImageField(upload_to='uploaded_pictures')),
                ('image_context', models.TextField(default='a')),
                ('image_date', models.DateTimeField(auto_now_add=True)),
                ('chart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.chart')),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.AddField(
            model_name='chart',
            name='disease',
            field=models.ManyToManyField(related_name='charts', to='emr.disease'),
        ),
        migrations.AddField(
            model_name='chart',
            name='inspect',
            field=models.ManyToManyField(related_name='charts', to='emr.inspecttype'),
        ),
        migrations.AddField(
            model_name='chart',
            name='medical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.medicalpersonidentity'),
        ),
        migrations.AddField(
            model_name='chart',
            name='medication',
            field=models.ManyToManyField(related_name='charts', to='emr.medication'),
        ),
        migrations.AddField(
            model_name='chart',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patientidentity'),
        ),
        migrations.AddField(
            model_name='chart',
            name='treatment',
            field=models.ManyToManyField(related_name='charts', to='emr.treatment'),
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('blood_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hemoglobin', models.FloatField(verbose_name='혈색소')),
                ('fasting_blood_sugar', models.FloatField(verbose_name='공복혈당')),
                ('total_cholesterol', models.FloatField(verbose_name='총 콜레스트롤')),
                ('hdl_cholesterol', models.FloatField(verbose_name='HDL-콜레스트롤')),
                ('triglycerides', models.FloatField(verbose_name='중성지방')),
                ('ldl_cholesterol', models.FloatField(verbose_name='LDL-콜레스트롤')),
                ('serum_creatinine', models.FloatField(verbose_name='혈청크레아티닌')),
                ('glomerular_filtration_rate', models.FloatField(verbose_name='신사구체여과율')),
                ('ast', models.FloatField(verbose_name='AST')),
                ('alt', models.FloatField(verbose_name='ALT')),
                ('gamma_gt', models.FloatField(verbose_name='감마지피티')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emr.patientidentity')),
            ],
            options={
                'db_table': 'blood',
            },
        ),
    ]
