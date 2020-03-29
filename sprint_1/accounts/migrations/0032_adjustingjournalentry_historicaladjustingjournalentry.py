# Generated by Django 3.0.2 on 2020-03-29 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0031_merge_20200311_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAdjustingJournalEntry',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Ajournal_name', models.CharField(db_index=True, max_length=300)),
                ('Ajournal_number', models.PositiveIntegerField(db_index=True)),
                ('Ajournal_description', models.TextField(blank=True, null=True)),
                ('Ajournal_debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Ajournal_credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Asource_document', models.TextField(blank=True, max_length=100, null=True)),
                ('Astatus', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Rejected')], default=1)),
                ('Adate', models.DateField(blank=True, editable=False)),
                ('Areason_for_rejection', models.CharField(blank=True, default='', max_length=1000)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.UserAccount')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical adjusting journal entry',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='AdjustingJournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ajournal_name', models.CharField(max_length=300, unique=True)),
                ('Ajournal_number', models.PositiveIntegerField(unique=True)),
                ('Ajournal_description', models.TextField(blank=True, null=True)),
                ('Ajournal_debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Ajournal_credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Asource_document', models.FileField(blank=True, null=True, upload_to='source_docs')),
                ('Astatus', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Rejected')], default=1)),
                ('Adate', models.DateField(auto_now_add=True)),
                ('Areason_for_rejection', models.CharField(blank=True, default='', max_length=1000)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserAccount')),
            ],
        ),
    ]