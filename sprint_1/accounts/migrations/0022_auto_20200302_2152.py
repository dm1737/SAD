# Generated by Django 3.0.2 on 2020-03-02 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20200302_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaljournal',
            name='user',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='user',
        ),
    ]
