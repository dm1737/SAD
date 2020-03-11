# Generated by Django 3.0.2 on 2020-03-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20200309_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaljournal',
            name='pending',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='pending',
        ),
        migrations.AddField(
            model_name='historicaljournal',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Rejected')], null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Rejected')], null=True),
        ),
    ]