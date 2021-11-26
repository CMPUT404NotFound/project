# Generated by Django 3.2.8 on 2021-11-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('jpeg', 'image/jpeg;base64'), ('markdown', 'text/markdown'), ('plain', 'text/plain'), ('png', 'image/png;base64'), ('app', 'application/base64')], default='plain', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('PU', 'PUBLIC'), ('PR', 'PRIVATE')], default='PU', max_length=8),
        ),
    ]
