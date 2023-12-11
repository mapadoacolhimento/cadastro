# Generated by Django 4.2.1 on 2023-12-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "volunteers",
            "0033_alter_volunteer_city_alter_volunteer_neighborhood_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="volunteeravailability",
            name="support_expertise",
            field=models.CharField(
                choices=[
                    ("Violência contra as mulheres", "Violência contra as mulheres"),
                    ("Assistência social", "Assistência social"),
                    ("Saúde mental", "Saúde mental"),
                    ("Psicologia clínica", "Psicologia clínica"),
                    ("Psicologia jurídica", "Psicologia jurídica"),
                    ("Psicologia social", "Psicologia social"),
                    ("Terapia sistêmica/familiar", "Terapia sistêmica/familiar"),
                    ("Serviços públicos", "Serviços públicos"),
                    ("Sócio-Histórica", "Sócio-Histórica"),
                    ("Não tenho experiência", "Não tenho experiência"),
                    ("Outros", "Outros"),
                    ("Violência de Gênero", "Violência de Gênero"),
                    ("Família", "Família"),
                    ("Penal", "\tPenal"),
                    ("Trabalhista", "Trabalhista"),
                    ("Cível", "Cível"),
                    ("Administrativo", "Administrativo"),
                    ("Empresarial", "Empresarial"),
                    ("Tributário", "Tributário"),
                    ("Digital", "\tDigital"),
                    ("Ambiental\t", "Ambiental"),
                    ("Outros", "Outros"),
                ],
                max_length=200,
            ),
        ),
    ]
