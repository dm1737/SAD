# Generated by Django 3.0.2 on 2020-02-13 01:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20200210_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUserAccount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('account_name', models.CharField(db_index=True, max_length=300)),
                ('account_number', models.IntegerField(db_index=True)),
                ('account_description', models.TextField()),
                ('account_category', models.CharField(max_length=300)),
                ('account_subcategory', models.CharField(max_length=300)),
                ('initial_balance', models.DecimalField(decimal_places=2, max_digits=10)),
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
