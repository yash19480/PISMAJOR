# Generated by Django 2.2.7 on 2019-11-27 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20191126_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='use_date',
        ),
    ]
