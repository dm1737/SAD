# Generated by Django 3.0.2 on 2020-03-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20200309_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaljournal',
            name='reason',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='journal',
            name='reason',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
