# Generated by Django 3.2.5 on 2021-11-04 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_last_pickup',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='one_time_pickup',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='suspend_end',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='suspend_start',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='weekly_pickup',
        ),
    ]
