# Generated by Django 3.0.6 on 2020-05-08 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="slug",
            field=models.SlugField(default=models.TextField()),
        ),
    ]
