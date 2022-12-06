# Generated by Django 3.1.8 on 2021-08-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0007_delete_favou'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('album_title', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('album_logo', models.CharField(max_length=10000)),
            ],
        ),
    ]
