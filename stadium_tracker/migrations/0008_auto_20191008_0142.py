# Generated by Django 2.2.2 on 2019-10-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium_tracker', '0007_auto_20190924_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedetails',
            name='game_body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gamedetails',
            name='game_headline',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
