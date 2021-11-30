# Generated by Django 3.2.9 on 2021-11-30 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Biblio', '0007_alter_post_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='UserPost', to=settings.AUTH_USER_MODEL),
        ),
    ]