from django import forms
from volunteers.fields import CharField, TextField, EmailField, ChoiceField, SelectField
from django.forms.models import ModelChoiceField
from volunteers.models import Cities
from .choices import (
    REGISTER_RISK_CHOICES,
    REGISTER_PROTECTION_CHOICES,
    STATE_CHOICES,
)


class RegisterStep0(forms.Form):
    titulo = "Você não está sozinha"
    subtitulo = "Com base nas suas respostas identificamos que você pode ser atendida pelo projeto. Agora precisamos de mais algumas informações para concluir o seu cadastro e te direcionar para o atendimento adequado. Vamos lá?"


class RegisterStep1(forms.Form):
    titulo = "Seus dados"
    subtitulo = ""
    first_name = CharField(label="Primeiro Nome", max_length=100)
    email = EmailField(label="E-mail", max_length=100)
    whatsapp = CharField(label="WhatsApp", max_length=11)

    state = SelectField(
        label="Estado",
        choices=STATE_CHOICES,
        widget=forms.Select(attrs={"id": "id_state"}),
    )

    city = ModelChoiceField(
        label="Cidade",
        queryset=Cities.objects.none(),
        empty_label="Selecione uma cidade",
        to_field_name="city_value",
        widget=forms.Select(attrs={"id": "id_city"}),
    )

    # Campo de texto para o bairro
    neighborhood = CharField(label="Bairro", max_length=100)

    def set_city_choices(self, state):
        cities = Cities.objects.filter(state=state)
        self.fields["city_value"].queryset = cities


class RegisterStep2(forms.Form):
    titulo = "Seus dados"
    subtitulo = ""

    color = SelectField(
        label="Cor",
        choices=(("ss", "Cor"), ("2", "2"), ("3", "3")),
    )

    pcd = SelectField(
        label="Você é uma pessoa com deficiência (PcD)?",
        choices=(
            ("", "Você é uma pessoa com deficiência (PcD)?"),
            ("Sim", "Sim"),
            ("Não", "Não"),
        ),
    )

    education = SelectField(
        label="Escolaridade",
        choices=(
            ("", "Escolaridade"),
            ("Ensino superior completo", "Ensino superior completo"),
            ("Ensino fundamental", "Ensino fundamental"),
        ),
    )


class RegisterStep3(forms.Form):
    titulo = "Dados da violência"
    subtitulo = ""

    author_violence = SelectField(
        label="Quem é ou foi o(a) autor(a) da violência?",
        choices=(
            ("", "Quem é ou foi o(a) autor(a) da violência?"),
            ("1", "1"),
            ("1", "1"),
        ),
    )

    how_long = SelectField(
        label="Há quanto tempo está sofrendo violência?",
        choices=(("1", "1"), ("1", "1")),
    )

    tell_us = forms.CharField(
        label="Se desejar, conte-nos um pouco sobre o seu caso (opcional):",
        max_length=100,
    )


class RegisterStep4(forms.Form):
    titulo = "Dados da violência"
    subtitulo = "Selecione as opções de fatores de risco que se aplicam ao seu caso:"

    risk_factor = forms.MultipleChoiceField(
        choices=REGISTER_RISK_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class RegisterStep5(forms.Form):
    titulo = "Dados da violência"
    subtitulo = "Selecione as opções de fatores de proteção que se aplicam ao seu caso:"

    protection_factor = forms.MultipleChoiceField(
        choices=REGISTER_PROTECTION_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class RegisterStep6(forms.Form):
    titulo = "Dados da violência"
    subtitulo = "Você está sendo atendida por algum serviço da rede de atendimento de violência contra as mulheres da região e ou por algum coletivo/ movimento?"

    options = (
        ("Sim, eu estou sendo atendida", "Sim, eu estou sendo atendida"),
        ("Não, eu não estou sendo atendida", "Não, eu não estou sendo atendida"),
    )

    already_served = forms.ChoiceField(
        choices=options,
        widget=forms.RadioSelect(attrs={"class": "radio-input"}),
    )


class RegisterStep7(forms.Form):
    titulo = "Sobre o acolhimento"
    subtitulo = "Você aceitaria ser atendida online?"

    options = (
        ("Sim, aceito ser atendida online", "Sim, aceito ser atendida online"),
        (
            "Não, só posso receber atendimento presencial",
            "Não, só posso receber atendimento presencial",
        ),
    )

    online_service = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class RegisterStep8(forms.Form):
    titulo = "Sobre o acolhimento"
    subtitulo = "Que tipo de acolhimento você precisa?"
    options = (
        ("Acolhimento psicológico", "Acolhimento psicológico"),
        ("Acolhimento jurídico", "Acolhimento jurídico"),
    )

    online_service = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class RegisterStep9(forms.Form):
    titulo = "Cadastro realizado com sucesso"
    subtitulo = "Nesse momento estamos buscando uma voluntária para para te atender"
