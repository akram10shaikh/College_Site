# Generated by Django 4.1.7 on 2023-07-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_remove_student_username_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('sname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('community', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=40)),
                ('pincode', models.CharField(max_length=20)),
                ('rollno10', models.CharField(max_length=20)),
                ('year10', models.CharField(max_length=20)),
                ('board10', models.CharField(max_length=40)),
                ('rollno12', models.CharField(max_length=20)),
                ('year12', models.CharField(max_length=20)),
                ('board12', models.CharField(max_length=40)),
                ('photo', models.FileField(upload_to='media/')),
            ],
        ),
    ]
