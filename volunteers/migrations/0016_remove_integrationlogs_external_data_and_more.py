# Generated by Django 4.2.1 on 2023-11-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0015_alter_integrationlogs_integration_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="integrationlogs",
            name="external_data",
        ),
        migrations.RemoveField(
            model_name="integrationlogs",
            name="form_data",
        ),
        migrations.AddField(
            model_name="integrationlogs",
            name="external_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="integrationlogs",
            name="form_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("psicologa", "Psicóloga"),
                    ("advogada", "Advogada"),
                    ("msr", "Msr"),
                ],
                max_length=15,
            ),
        ),
        migrations.AddField(
            model_name="integrationlogs",
            name="internal_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
