# Generated by Django 3.2.8 on 2021-12-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=100)),
                ('parentId', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
