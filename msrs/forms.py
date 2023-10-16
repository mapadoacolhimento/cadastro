from django import forms

from .choices import (
    GENDER_CHOICES,
    AGE_CHOICES,
    LOCAL_CHOICES,
    VIOLENCE_CHOICES,
    SERVICE_CHOICES,
    INCOME_CHOICES,
    TO_HAVE_CHOICES,
    TO_BE_CHOICES,
  
  
)

class MsrStep0(forms.Form):
    titulo = "Sobre você"
    subtitulo = "Qual a sua identidade de <span class='text-primary font-bold'>gênero</span>?"
  
    gender_select = forms.MultipleChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),
    )

class MsrStep1(forms.Form):
    titulo = "Sobre você"
    subtitulo = "Você é <span class='text-primary font-bold'>maior de 18 anos</span>?"
    
    majority = forms.MultipleChoiceField(
        choices=AGE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'})
    )

class MsrStep2(forms.Form):
    # message = forms.CharField(widget=forms.Textarea)
    titulo = "Sobre a violência"
    subtitulo = "A violência sofriada <span class='text-primary font-bold'>ocorreu no Brasil</span>?"
   
    locality = forms.MultipleChoiceField(
        choices=LOCAL_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep3(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de violência <span class='text-primary font-bold'>você sofreu ou está sofrendo </span>pelo fato de ser mulher?"
   
    types_of_violence = forms.MultipleChoiceField(
        choices=VIOLENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep4(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Você está em atendimento psicológico e/ou jurídico <span class='text-primary font-bold'>fora do Mapa do Acolhimento </span>?"
   
    public_service = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep5(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Defina qual valor corresponde <span class='text-primary font-bold'>a sua renda individual</span>:"
    income = forms.DecimalField(max_digits=10, decimal_places=2)
class MsrStep6(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Qual a sua <span class='text-primary font-bold'>situação de trabalho</span>?"

    has_dependents = forms.MultipleChoiceField(
        choices= INCOME_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep7(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Você tem <span class='text-primary font-bold'>dependentes financeiros</span>?"

    options = (
        ('Sim', 'Sim, eu tenho'),
        ('Não', 'Não, eu não tenho'),
    )

    financially_dependent = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep8(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = 'Você é <span class=\'text-primary font-bold\'>responsável financeiramente</span> pela renda familiar ("chefe de família")?'

    options = (
        ('Sim', 'Sim, eu sou'),
        ('Não', 'Não, eu não sou'),
    )

    financially_responsible = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep9(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Você possui <span class='text-primary font-bold'>bens móveis e/ou bens imóveis</span> em seu nome?"
    options = (
        ('Sim', 'Sim, eu tenho'),
        ('Não', 'Não, eu não tenho'),
    )

    properties = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

   

