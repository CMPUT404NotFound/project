# Generated by Django 3.2.8 on 2021-12-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='url of node')),
                ('netloc', models.CharField(default='', max_length=100, verbose_name='netloc of node')),
                ('allowIncoming', models.BooleanField()),
                ('allowOutgoing', models.BooleanField()),
                ('incomingName', models.CharField(default='defaultName', max_length=128)),
                ('outgoingName', models.CharField(default='defaultName', max_length=128)),
                ('incomingPassword', models.CharField(default='passpass', max_length=128)),
                ('outgoingPassword', models.CharField(default='passpass', max_length=128)),
                ('description', models.CharField(blank=True, default=False, max_length=300)),
            ],
        ),
    ]
