# Generated by Django 3.2.9 on 2021-12-02 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0009_profile_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
    ]
