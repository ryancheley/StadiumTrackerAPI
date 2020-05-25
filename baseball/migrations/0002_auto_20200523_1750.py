# Generated by Django 3.0.6 on 2020-05-23 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferences',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='conferences',
            name='league_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.League'),
        ),
        migrations.AddField(
            model_name='conferences',
            name='mlb_api_conference_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conferences',
            name='name',
            field=models.CharField(blank=True, max_length=23, null=True),
        ),
        migrations.AddField(
            model_name='conferences',
            name='name_short',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='conferences',
            name='sport_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Sport'),
        ),
        migrations.AddField(
            model_name='division',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='league_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.League'),
        ),
        migrations.AddField(
            model_name='division',
            name='mlb_api_division_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='name',
            field=models.CharField(blank=True, max_length=38, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='name_short',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='sport_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Sport'),
        ),
        migrations.AddField(
            model_name='league',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='league',
            name='mlb_api_league_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='league',
            name='name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='league',
            name='name_short',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='league',
            name='number_of_teams',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='league',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='league',
            name='sport_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Sport'),
        ),
        migrations.AddField(
            model_name='team',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='division_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Division'),
        ),
        migrations.AddField(
            model_name='team',
            name='file_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='first_year_of_play',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='league_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.League'),
        ),
        migrations.AddField(
            model_name='team',
            name='location_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='mlb_api_team_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='parent_organization_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Team'),
        ),
        migrations.AddField(
            model_name='team',
            name='short_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='sport_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Sport'),
        ),
        migrations.AddField(
            model_name='team',
            name='team_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='venue_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseball.Venue'),
        ),
        migrations.AddField(
            model_name='venue',
            name='mlb_api_venue_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='name',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
    ]