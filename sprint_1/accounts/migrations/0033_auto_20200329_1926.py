# Generated by Django 3.0.2 on 2020-03-29 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_adjustingjournalentry_historicaladjustingjournalentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Adate',
            new_name='Adjusted_date',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Ajournal_credit',
            new_name='Adjusted_journal_credit',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Ajournal_debit',
            new_name='Adjusted_journal_debit',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Ajournal_description',
            new_name='Adjusted_journal_description',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Ajournal_name',
            new_name='Adjusted_journal_name',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Ajournal_number',
            new_name='Adjusted_journal_number',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Areason_for_rejection',
            new_name='Adjusted_reason_for_rejection',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Asource_document',
            new_name='Adjusted_source_document',
        ),
        migrations.RenameField(
            model_name='adjustingjournalentry',
            old_name='Astatus',
            new_name='Adjusted_status',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Adate',
            new_name='Adjusted_date',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Ajournal_credit',
            new_name='Adjusted_journal_credit',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Ajournal_debit',
            new_name='Adjusted_journal_debit',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Ajournal_description',
            new_name='Adjusted_journal_description',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Ajournal_name',
            new_name='Adjusted_journal_name',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Ajournal_number',
            new_name='Adjusted_journal_number',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Areason_for_rejection',
            new_name='Adjusted_reason_for_rejection',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Asource_document',
            new_name='Adjusted_source_document',
        ),
        migrations.RenameField(
            model_name='historicaladjustingjournalentry',
            old_name='Astatus',
            new_name='Adjusted_status',
        ),
    ]
