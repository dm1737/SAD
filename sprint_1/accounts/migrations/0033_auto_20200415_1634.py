# Generated by Django 3.0.4 on 2020-04-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20200415_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaljournal',
            name='journal_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='journal_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
