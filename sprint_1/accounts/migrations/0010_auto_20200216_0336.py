# Generated by Django 3.0.2 on 2020-02-16 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_auto_20200213_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_initial', models.CharField(blank=True, max_length=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Accountant'), (2, 'Manager'), (3, 'Admin')], null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='account_category',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='account_name',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='account_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='account_subcategory',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='credit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='debit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='initial_balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='order',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='HistoricalUserAccount',
        ),
    ]