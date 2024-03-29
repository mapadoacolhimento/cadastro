from django import forms
from volunteers.fields import CharField, TextField, EmailField, ChoiceField, SelectField

from .choices import (
    GENDER_CHOICES,
    AGE_CHOICES,
    LOCAL_CHOICES,
    PHYSICAL_VIOLENCE_CHOICES,
    PSYCH_VIOLENCE_CHOICES,
    SEXUAL_VIOLENCE_CHOICES,
    DIGITAL_VIOLENCE_CHOICES,
    PROPERTY_VIOLENCE_CHOICES,
    OBSTETRIC_VIOLENCE_CHOICES,
    SERVICE_CHOICES,
    INCOME_CHOICES,
)


class MsrStep0(forms.Form):
    titulo = "Sobre você"
    subtitulo = (
        "Qual a sua identidade de <span class='text-primary font-bold'>gênero</span>?"
    )
    gender_options = GENDER_CHOICES

    gender_select = forms.ChoiceField(
        choices=gender_options,
        widget=forms.RadioSelect(attrs={"class": "custom-radio"}),
    )


class MsrStep1(forms.Form):
    titulo = "Sobre você"
    subtitulo = "Você é <span class='text-primary font-bold'>maior de 18 anos</span>?"
    age = AGE_CHOICES

    majority = forms.ChoiceField(
        choices=age,
        widget=forms.RadioSelect(attrs={"class": "custom-radio"}),
    )


class MsrStep2(forms.Form):
    # message = forms.CharField(widget=forms.Textarea)
    age = forms.CharField(max_length=3)
    titulo = "Sobre a violência"
    subtitulo = "A violência sofriada <span class='text-primary font-bold'>ocorreu no Brasil</span>?"
    age = LOCAL_CHOICES

    locality = forms.ChoiceField(
        choices=age,
        widget=forms.RadioSelect(attrs={"class": "custom-radio"}),
    )


class MsrStep3(forms.Form):
    titulo = "Ainda sobre a violência"
    subtitulo = "Agora compartilhe conosco como a violência aconteceu. Sinta-se à vontade para escolher múltiplas opções, lembrando que não é obrigatório ter vivenciado todos os tipos de violência..."

    agree = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={"class": "custom-mini-checkbox"}),
    )


class MsrStep4(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de <span class='text-primary font-bold'>violência física</span> você sofreu ou está sofrendo pelo fato de ser mulher?"

    types_of_physical_violence = forms.MultipleChoiceField(
        choices=PHYSICAL_VIOLENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class MsrStep5(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de  <span class='text-primary font-bold'>violência psicológica</span> você sofreu ou está sofrendo pelo fato de ser mulher?"

    types_of_psych_violence = forms.MultipleChoiceField(
        choices=PSYCH_VIOLENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class MsrStep6(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de <span class='text-primary font-bold'>violência sexual</span> você sofreu ou está sofrendo pelo fato de ser mulher?"

    types_of_sexual_violence = forms.MultipleChoiceField(
        choices=SEXUAL_VIOLENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class MsrStep7(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de <span class='text-primary font-bold'>violência digital</span> você sofreu ou está sofrendo pelo fato de ser mulher?"

    types_of_sexual_violence = forms.MultipleChoiceField(
        choices=DIGITAL_VIOLENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class MsrStep8(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de <span class='text-primary font-bold'>violência patrimonial</span> você sofreu ou está sofrendo pelo fato de ser mulher?"

    types_of_sexual_violence = forms.MultipleChoiceField(
        choices=PROPERTY_VIOLENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class MsrStep9(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de <span class='text-primary font-bold'>violência obstétrica</span> você sofreu ou está sofrendo pelo fato de ser mulher?"

    types_of_sexual_violence = forms.MultipleChoiceField(
        choices=OBSTETRIC_VIOLENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class MsrStep10(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Você está em atendimento psicológico e/ou jurídico <span class='text-primary font-bold'>fora do Mapa do Acolhimento </span>?"

    other_service = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class MsrStep11(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Defina qual valor corresponde <span class='text-primary font-bold'>a sua renda individual</span>:"

    income = forms.CharField(widget=forms.HiddenInput)


class MsrStep12(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = (
        "Qual a sua <span class='text-primary font-bold'>situação de trabalho</span>?"
    )

    has_dependents = forms.MultipleChoiceField(
        choices=INCOME_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


#  types_of_violence = forms.ChoiceField(
#         choices=age,
#         widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
class MsrStep13(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = (
        "Você tem <span class='text-primary font-bold'>dependentes financeiros</span>?"
    )

    options = (
        ("Sim", "Sim, eu tenho"),
        ("Não", "Não, eu não tenho"),
    )

    financially_dependent = forms.ChoiceField(
        choices=options,
        widget=forms.RadioSelect(attrs={"class": "custom-radio"}),
    )


class MsrStep14(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Você é <span class='text-primary font-bold'>responsável financeiramente</span> pela renda familiar (\"chefe de família\")?"

    options = (
        ("Sim", "Sim, eu sou"),
        ("Não", "Não, eu não sou"),
    )

    financially_responsible = forms.ChoiceField(
        choices=options,
        widget=forms.RadioSelect(attrs={"class": "custom-radio"}),
    )


class MsrStep15(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Você possui <span class='text-primary font-bold'>bens móveis e/ou bens imóveis</span> em seu nome?"
    options = (
        ("Sim", "Sim, eu tenho"),
        ("Não", "Não, eu não tenho"),
    )

    properties = forms.ChoiceField(
        choices=options,
        widget=forms.RadioSelect(attrs={"class": "custom-radio"}),
    )
