from django import forms

from .fields import CharField, ChoiceField, EmailField, MaskField, ZipCodeField


class PeopleForm(forms.Form):
    first_name = CharField(label="Primeiro nome")
    last_name = CharField(label="Sobrenome", required=False)
    email = EmailField(label="Seu melhor e-mail")
    whatsapp = MaskField(label="Número de telefone", mask="(00) 0 0000-0000")
    zipcode = ZipCodeField(label="CEP de atendimento", mask="00000-000")

    template_name = "forms/daisyui-form.html"


COLOR_CHOICES = (
    ("", "Cor"),
    ("Preta", "Preta"),
    ("Parda", "Parda"),
    ("Indígena", "Indígena"),
    ("Amarela", "Amarela"),
    ("Branca", "Branca"),
)

GENDER_CHOICES = (
    ("", "Identidade de gênero"),
    ("Mulher cisgênero", "Mulher cisgênero (que se identifica com o sexo que lhe foi designado ao nascer)"),
    ("Mulher transgênero/travesti",
     "Mulher transgênero/travesti (possui outra identidade de gênero, diferente da que lhe foi designada ao nascer)"),
    ("Prefiro não responder", "Prefiro não responder"),
)


class People2Form(forms.Form):
    color = ChoiceField(label="Cor", choices=COLOR_CHOICES)
    gender = ChoiceField(label="Identidade de gênero", choices=GENDER_CHOICES)
    phone = MaskField(label="Telefone de atendimento com DDD",
                      mask="(00) 0 0000-0000")

    document_number = MaskField(label="CRP", mask="00/000000")
    # document_number = MaskField(label="OAB", mask="(00) 0 0000-0000")

    template_name = "forms/daisyui.html"
