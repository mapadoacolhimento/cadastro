# Generated by Django 4.2.1 on 2023-11-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0018_volunteeravailability_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteeravailability",
            name="state",
            field=models.CharField(max_length=2),
        ),
    ]
