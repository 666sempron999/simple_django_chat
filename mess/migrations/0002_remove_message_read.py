# Generated by Django 3.0.1 on 2019-12-24 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
    ]
