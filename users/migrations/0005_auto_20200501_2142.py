# Generated by Django 3.0.5 on 2020-05-01 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_auto_20191005_0305"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="favorite_team",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (109, "Arizona Diamondbacks"),
                    (144, "Atlanta Braves"),
                    (110, "Baltimore Orioles"),
                    (111, "Boston Red Sox"),
                    (112, "Chicago Cubs"),
                    (145, "Chicago White Sox"),
                    (113, "Cincinnati Reds"),
                    (114, "Cleveland Indians"),
                    (115, "Colorado Rockies"),
                    (116, "Detroit Tigers"),
                    (117, "Houston Astros"),
                    (118, "Kansas City Royals"),
                    (108, "Los Angeles Angels"),
                    (119, "Los Angeles Dodgers"),
                    (146, "Miami Marlins"),
                    (158, "Milwaukee Brewers"),
                    (142, "Minnesota Twins"),
                    (121, "New York Mets"),
                    (147, "New York Yankees"),
                    (133, "Oakland Athletics"),
                    (143, "Philadelphia Phillies"),
                    (134, "Pittsburgh Pirates"),
                    (135, "San Diego Padres"),
                    (137, "San Francisco Giants"),
                    (136, "Seattle Mariners"),
                    (138, "St. Louis Cardinals"),
                    (139, "Tampa Bay Rays"),
                    (140, "Texas Rangers"),
                    (141, "Toronto Blue Jays"),
                    (120, "Washington Nationals"),
                ],
                null=True,
            ),
        ),
    ]
