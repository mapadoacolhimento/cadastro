# Generated by Django 4.2.1 on 2023-11-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0014_volunteer_ocuppation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="integrationlogs",
            name="integration",
            field=models.CharField(
                blank=True,
                choices=[
                    ("bonde", "Bonde"),
                    ("moodle", "Moodle"),
                    ("zendesk", "Zendesk"),
                ],
                max_length=15,
            ),
        ),
        migrations.AlterModelTable(
            name="integrationlogs",
            table="integrations_logs",
        ),
        migrations.AlterModelTable(
            name="volunteer",
            table="volunteers",
        ),
    ]
