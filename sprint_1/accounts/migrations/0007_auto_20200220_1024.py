# Generated by Django 3.0.2 on 2020-02-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='attempts',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
