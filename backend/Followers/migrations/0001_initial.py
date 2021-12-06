# Generated by Django 3.2.8 on 2021-12-06 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=40, primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestor', models.CharField(max_length=100)),
                ('requestee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
