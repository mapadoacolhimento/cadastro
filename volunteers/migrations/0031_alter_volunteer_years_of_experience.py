# Generated by Django 4.2.1 on 2023-11-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0030_alter_volunteer_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteer",
            name="years_of_experience",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Não tenho experiência ", "Não tenho experiência"),
                    ("Menos de 6 meses", "Menos de 6 meses"),
                    ("Menos de 1 ano", "Menos de 1 ano"),
                    ("Menos de 2 anos", "Menos de 2 anos"),
                    ("Menos de 5 anos", "Menos de 5 anos"),
                    ("Menos de 10 anos", "Menos de 10 anos"),
                ],
                max_length=100,
            ),
        ),
    ]