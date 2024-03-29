# Generated by Django 4.2.1 on 2023-07-25 20:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0008_rename_created_date_formdata_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IntegrationLogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("bonde", "Bonde"),
                            ("moodle", "Moodle"),
                            ("action_network", "Action Network"),
                        ],
                        max_length=15,
                    ),
                ),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("status", models.CharField(max_length=15)),
                ("error", models.CharField(max_length=200)),
                ("data", models.JSONField(blank=True, default=dict)),
                (
                    "form_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="volunteers.formdata"
                    ),
                ),
            ],
        ),
    ]
