# Generated by Django 3.0.2 on 2020-02-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200122_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLockout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, unique=True)),
                ('attempts', models.IntegerField()),
            ],
        ),
    ]
