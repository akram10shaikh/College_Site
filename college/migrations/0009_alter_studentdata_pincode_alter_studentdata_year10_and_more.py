# Generated by Django 4.1.7 on 2023-07-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_alter_studentdata_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='pincode',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='year10',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='year12',
            field=models.IntegerField(default=''),
        ),
    ]
