# Generated by Django 3.2.9 on 2021-11-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0003_auto_20211114_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='myfolder/'),
        ),
    ]
