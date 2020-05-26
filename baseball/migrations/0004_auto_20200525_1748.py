# Generated by Django 3.0.6 on 2020-05-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0003_auto_20200523_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='abbreviation',
            field=models.CharField(blank=True, default='None', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='league',
            name='number_of_teams',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]