# Generated by Django 3.0.2 on 2020-02-24 21:29

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_auto_20200220_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=300, unique=True)),
                ('account_number', models.PositiveIntegerField(unique=True)),
                ('account_description', models.TextField()),
                ('account_category', models.CharField(max_length=300)),
                ('account_subcategory', models.CharField(max_length=300)),
                ('initial_balance', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_created', models.DateTimeField(default=datetime.datetime.now)),
                ('order', models.CharField(max_length=300)),
                ('statement', models.FileField(null=True, upload_to='')),
                ('comment', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalUserAccount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('account_name', models.CharField(db_index=True, max_length=300)),
                ('account_number', models.PositiveIntegerField(db_index=True)),
                ('account_description', models.TextField()),
                ('account_category', models.CharField(max_length=300)),
                ('account_subcategory', models.CharField(max_length=300)),
                ('initial_balance', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_created', models.DateTimeField(default=datetime.datetime.now)),
                ('order', models.CharField(max_length=300)),
                ('statement', models.TextField(max_length=100, null=True)),
                ('comment', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user account',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]