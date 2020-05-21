# Generated by Django 3.0.6 on 2020-05-20 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stadium_tracker', '0015_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mlb_api_league_id', models.IntegerField()),
                ('league_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='division',
            name='mlb_api_league_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='division',
            name='mlb_api_sport_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadium_tracker.League'),
        ),
    ]