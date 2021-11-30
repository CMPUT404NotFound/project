# Generated by Django 3.2.8 on 2021-11-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_contenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('markdown', 'text/markdown'), ('plain', 'text/plain'), ('jpeg', 'image/jpeg;base64'), ('app', 'application/base64'), ('png', 'image/png;base64')], default='plain', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('PU', 'PUBLIC'), ('PR', 'PRIVATE')], default='PU', max_length=8),
        ),
    ]
