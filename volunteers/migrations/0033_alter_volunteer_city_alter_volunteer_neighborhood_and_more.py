# Generated by Django 4.2.1 on 2023-12-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0032_volunteer_street_alter_volunteer_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteer",
            name="city",
            field=models.CharField(
                default="not_found", max_length=100, verbose_name="Cidade"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="neighborhood",
            field=models.CharField(
                default="not_found", max_length=100, verbose_name="Bairro"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="state",
            field=models.CharField(
                default="not_found", max_length=9, verbose_name="Estado"
            ),
            preserve_default=False,
        ),
    ]