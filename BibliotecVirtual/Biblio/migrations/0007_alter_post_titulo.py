# Generated by Django 3.2.9 on 2021-11-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0006_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=51),
        ),
    ]