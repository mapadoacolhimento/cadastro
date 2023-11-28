# Generated by Django 4.2.1 on 2023-11-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("volunteers", "0025_rename_ocuppation_volunteer_occupation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteer",
            name="phone",
            field=models.CharField(
                max_length=100, verbose_name="Telefone de atendimento"
            ),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="register_number",
            field=models.CharField(max_length=400, verbose_name="Numero de registro"),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="whatsapp",
            field=models.CharField(max_length=100, verbose_name="Whatsapp"),
        ),
    ]