# Generated by Django 3.2.9 on 2021-11-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_alter_comment_contenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contentType',
            field=models.CharField(choices=[('P', 'text/plain'), ('M', 'text/markdown')], default='P', max_length=1, verbose_name='contentType'),
        ),
    ]
