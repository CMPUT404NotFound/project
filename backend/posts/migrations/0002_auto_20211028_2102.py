# Generated by Django 3.2.7 on 2021-10-28 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(blank=True, max_length=200, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='visibility',
            field=models.CharField(choices=[('PU', 'PUBLIC'), ('PR', 'PRIVATE')], default='PU', max_length=8),
        ),
        migrations.AlterField(
            model_name='postsmanager',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]