# Generated by Django 4.2.1 on 2023-11-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("msrs", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="msrs",
            name="violence",
        ),
        migrations.AddField(
            model_name="msrs",
            name="digital_violence",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Tive vazamento/compartilhamento na internet de minhas informações pessoais e dados sem meu consentimento",
                        "Tive vazamento/compartilhamento na internet de minhas informações pessoais e dados sem meu consentimento",
                    ),
                    (
                        "Tive vazamento/compartilhamento na internet de minhas imagens íntimas",
                        "Tive vazamento/compartilhamento na internet de minhas imagens íntimas",
                    ),
                    (
                        "Sofri stalking online (perseguição ou observação obsessiva)",
                        "Sofri stalking online (perseguição ou observação obsessiva)",
                    ),
                    (
                        "Não estou sofrendo violência digital",
                        "Não estou sofrendo violência digital",
                    ),
                ],
                max_length=200,
                verbose_name="Tipo de violência digital",
            ),
        ),
        migrations.AddField(
            model_name="msrs",
            name="obstetric_violence",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Alteraram o processo natural do parto sem meu consentimento voluntário",
                        "Alteraram o processo natural do parto sem meu consentimento voluntário",
                    ),
                    (
                        "Sofri abusos e maus-tratos durante a minha gestação",
                        "Sofri abusos e maus-tratos durante a minha gestação",
                    ),
                    (
                        "Sofri abusos e maus-tratos no momento do meu parto",
                        "Sofri abusos e maus-tratos no momento do meu parto",
                    ),
                    (
                        "Não estou sofrendo violência obstétrica",
                        "Não estou sofrendo violência obstétrica",
                    ),
                ],
                max_length=100,
                verbose_name="Tipo de violência obstétrica",
            ),
        ),
        migrations.AddField(
            model_name="msrs",
            name="physical_violence",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Soco", "Soco"),
                    ("Chute", "Chute"),
                    ("Tapa", "Tapa"),
                    ("Empurrão", "Empurrão"),
                    ("Puxão de cabelo", "Puxão de cabelo"),
                    ("Queimadura", "Queimadura"),
                    ("Enforcamento", "Enforcamento"),
                    ("Sufocamento", "Sufocamento"),
                    ("Tiro", "Tiro"),
                    ("Afogamento", "Afogamento"),
                    ("Paulada", "Paulada"),
                    ("Estrangulamento", "Estrangulamento"),
                    ("Facada", "Facada"),
                    (
                        "Me exigiu práticas sexuais que eu não gosto",
                        "Me exigiu práticas sexuais que eu não gosto",
                    ),
                    (
                        "Fui forçada à alguma prática sexual na intenção de corrigirem minha orientação sexual",
                        "Fui forçada à alguma prática sexual na intenção de corrigirem minha orientação sexual",
                    ),
                    (
                        "Não estou sofrendo violência física",
                        "Não estou sofrendo violência física",
                    ),
                ],
                max_length=100,
                verbose_name="Tipo de violência física",
            ),
        ),
        migrations.AddField(
            model_name="msrs",
            name="property_violence",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Ocultou bens e propriedades", "Ocultou bens e propriedades"),
                    ("Controlou meu dinheiro", "Controlou meu dinheiro"),
                    (
                        "Me impediu de ter acesso ao dinheiro",
                        "Me impediu de ter acesso ao dinheiro",
                    ),
                    ("Destruiu meus objetos", "Destruiu meus objetos"),
                    ("Me extorquiu", "Me extorquiu"),
                    (
                        "Me impediu de ter acesso a conta bancária ou outros bens",
                        "Me impediu de ter acesso a conta bancária ou outros bens",
                    ),
                    (
                        "Não estou sofrendo violência patrimonial",
                        "Não estou sofrendo violência patrimonial",
                    ),
                ],
                max_length=100,
                verbose_name="Tipo de violência patrimonial",
            ),
        ),
        migrations.AddField(
            model_name="msrs",
            name="psych_violence",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Fui controlada", "Fui controlada"),
                    ("Fui criticada", "Fui criticada"),
                    ("Fui humilhada", "Fui humilhada"),
                    ("Fui insultada", "Fui insultada"),
                    (
                        "Se/me negou a usar preservativo",
                        "Se/me negou a usar preservativo",
                    ),
                    (
                        "Tive minha identidade inviabilizada e negada",
                        "Tive minha identidade inviabilizada e negada",
                    ),
                    ("Fui isolada", "Fui isolada"),
                    (
                        "Não me permitiu usar certos tipos de roupa",
                        "Não me permitiu usar certos tipos de roupa",
                    ),
                    ("Fui xingada", "Fui xingada"),
                    ("Fui desautorizada", "Fui desautorizada"),
                    ("Não me deixou trabalhar", "Não me deixou trabalhar"),
                    (
                        "Me negou o direito a métodos contraceptivos",
                        "Me negou o direito a métodos contraceptivos",
                    ),
                    ("Fui vigiada", "Fui vigiada"),
                    ("Fui perseguida e ameaçada", "Fui perseguida e ameaçada"),
                    ("Proibida de ir ao médico", "Proibida de ir ao médico"),
                    (
                        "Não estou sofrendo violência psicológica",
                        "Não estou sofrendo violência psicológica",
                    ),
                ],
                max_length=100,
                verbose_name="Tipo de violência psicológica",
            ),
        ),
        migrations.AddField(
            model_name="msrs",
            name="sexual_violence",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Se/me negou a usar preservativo",
                        "Se/me negou a usar preservativo",
                    ),
                    (
                        "Me negou o direito a métodos contraceptivos",
                        "Me negou o direito a métodos contraceptivos",
                    ),
                    (
                        "Fui forçada à alguma prática sexual na intenção ",
                        "de corrigirem minha orientação sexual",
                    ),
                    (
                        "Me exigiu práticas sexuais que eu não gosto",
                        "Me exigiu práticas sexuais que eu não gosto",
                    ),
                    (
                        "Não estou sofrendo violência sexual",
                        "Não estou sofrendo violência sexual",
                    ),
                ],
                max_length=100,
                verbose_name="Tipo de violência sexual",
            ),
        ),
    ]
