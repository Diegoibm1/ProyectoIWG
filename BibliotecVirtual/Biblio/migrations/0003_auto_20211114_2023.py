# Generated by Django 3.2.9 on 2021-11-14 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0002_auto_20211114_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='archivo',
        ),
        migrations.AlterField(
            model_name='post',
            name='ramo',
            field=models.CharField(max_length=7),
        ),
    ]