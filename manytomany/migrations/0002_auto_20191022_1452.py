# Generated by Django 2.2.5 on 2019-10-22 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(related_name='patients', to='manytomany.Doctor'),
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
