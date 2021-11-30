# Generated by Django 3.2.8 on 2021-11-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0005_alter_inboxitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboxitem',
            name='type',
            field=models.CharField(choices=[('F', 'Follow'), ('L', 'Like'), ('P', 'Post')], default='P', max_length=1),
        ),
    ]