# Generated by Django 3.0.6 on 2020-05-23 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0004_auto_20200523_2359'),
        ('stadium_tracker', '0024_gamedetails_stadium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedetails',
            name='stadium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Venue'),
        ),
    ]
