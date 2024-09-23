from django.test import TestCase
from volunteers.zendesk import format_fields_of_work
from volunteers.choices import FOW_CHOICES

formated_fields_of_work = [
    "violencia_contra_as_mulheres",
    "assistencia_social",
    "saude_mental",
    "psicologia_clinica",
    "psicologia_juridica",
    "psicologia_social",
    "terapia_sistemica_familiar",
    "servicos_publicos",
    "socio_historica",
    "nao_tenho_experiencia",
    "outros",
    "violencia_de_genero",
    "familia",
    "penal",
    "trabalhista",
    "civel",
    "administrativo",
    "empresarial",
    "tributario",
    "digital",
    "ambiental",
    "outros"
]

class TestFormatFieldOfWork(TestCase):

    def test_format_fields_of_work(self):
        for i,fow in enumerate(formated_fields_of_work):
            self.assertEqual(format_fields_of_work([FOW_CHOICES[i][1]]), [fow])