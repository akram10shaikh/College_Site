# Generated by Django 4.1.7 on 2023-07-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
    ]
