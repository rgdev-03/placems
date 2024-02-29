# Generated by Django 5.0.2 on 2024-02-28 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('batch_code', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=255)),
                ('branch_code', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('staff_code', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('staff_type', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_mange.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('USN', models.CharField(max_length=20, unique=True)),
                ('sec', models.CharField(max_length=1, null=True)),
                ('sem', models.CharField(max_length=1, null=True)),
                ('roll_no', models.CharField(max_length=10, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('mobile', models.CharField(max_length=15)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_mange.batch')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_mange.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_type', models.CharField(max_length=50)),
                ('project_name', models.CharField(max_length=255)),
                ('project_specification', models.TextField()),
                ('project_repo_url', models.URLField(null=True)),
                ('certificate', models.ImageField(null=True, upload_to='project_certificates/')),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_mange.student')),
            ],
        ),
        migrations.CreateModel(
            name='Certi_Skills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('certification_name', models.CharField(max_length=255)),
                ('certi_s_date', models.DateField()),
                ('certi_e_date', models.DateField()),
                ('image_upload', models.ImageField(null=True, upload_to='certification_images/')),
                ('certi_outcomes', models.TextField(null=True)),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_mange.student')),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('event_name', models.CharField(max_length=255)),
                ('certification', models.ImageField(null=True, upload_to='achievement_certificates/')),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_mange.student')),
            ],
        ),
        migrations.CreateModel(
            name='Academic_Per',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acad_sem', models.CharField(max_length=255)),
                ('acad_sgpa', models.CharField(max_length=255)),
                ('sem10th', models.CharField(max_length=255)),
                ('sem12th_diploma', models.CharField(max_length=255)),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_mange.student')),
            ],
        ),
    ]
