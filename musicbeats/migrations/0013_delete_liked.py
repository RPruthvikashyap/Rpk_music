# Generated by Django 3.1.8 on 2021-08-15 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0012_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='liked',
        ),
    ]