# Generated by Django 3.0.6 on 2020-05-19 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium_tracker', '0011_gamedetails_view_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leagues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=255)),
            ],
        ),
    ]
