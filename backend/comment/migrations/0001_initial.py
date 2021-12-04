# Generated by Django 3.2.8 on 2021-12-04 10:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, max_length=100, verbose_name='id to local or foreign author')),
                ('comment', models.TextField(blank=True, default='', max_length=360, verbose_name='comment')),
                ('contentType', models.CharField(choices=[('P', 'text/plain'), ('M', 'text/markdown')], default='P', max_length=1, verbose_name='contentType')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='published')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.post')),
            ],
        ),
    ]
