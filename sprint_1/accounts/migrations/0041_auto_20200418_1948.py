# Generated by Django 3.0.2 on 2020-04-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20200418_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='statements',
            name='Beginning_Balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statements',
            name='Divedends',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
