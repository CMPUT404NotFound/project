# Generated by Django 3.2.8 on 2021-12-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newUserRequireActivation', models.BooleanField(default=False, verbose_name='New User Require Activation')),
            ],
        ),
    ]
