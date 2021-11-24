# Generated by Django 3.2.8 on 2021-11-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0005_alter_inboxitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboxitem',
            name='type',
            field=models.CharField(choices=[('P', 'Post'), ('F', 'Follow'), ('L', 'Like')], default='P', max_length=1),
        ),
    ]
