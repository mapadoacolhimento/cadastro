from django import forms

class MsrStep0(forms.Form):
    titulo = "Sobre você"
    subtitulo = "Qual a sua identidade de gênero?"
    gender_options = (
        ('cis', 'Eu sou uma mulher cis'),
        ('trans', 'Eu sou uma mulher trans/travesti'),
        ('nda', 'Não me identifico como mulher'),
    )

    gender_select = forms.MultipleChoiceField(
        choices=gender_options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),
    )

class MsrStep1(forms.Form):
    titulo = "Sobre você"
    subtitulo = "Você é maior de 18 anos?"
    age = (
        ('maior', 'Eu sou maior de 18 anos'),
        ('menor', 'Eu sou menor de 18 anos'),
    )

    majority = forms.MultipleChoiceField(
        choices=age,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'})
    )

class MsrStep2(forms.Form):
    # message = forms.CharField(widget=forms.Textarea)
    age = forms.CharField(max_length=3)
    titulo = "Sobre a violência"
    subtitulo = "A violência sofriada ocorreu no Brasil?"
    age = (
        ('brasil', 'Sim, dentro do território brasileiro'),
        ('internacional', 'Não, aconteceu em outro país'),
    )

    types_of_violence = forms.MultipleChoiceField(
        choices=age,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep3(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Quais o(s) tipo(s) de violência você sofreu ou está sofrendo pelo fato de ser mulher?"
    violence = (
        ('Fui humilhada', 'Fui humilhada'),
        ('Levei um soco', 'Levei um soco'),
        ('Fui ameaçada', 'Fui ameaçada'),
        ('Levei um chute e/ou tapa', 'Levei um chute e/ou tapa'),
        ('Sofri abusos e maus-tratos', 'Sofri abusos e maus-tratos'),
        ('Se/me negou a usar preservativo', 'Se/me negou a usar preservativo'),
        ('Fui perseguida e/ou vigiada', 'Fui perseguida e/ou vigiada'),
        ('Me expôs na internet', 'Me expôs na internet'),
        ('Fui forçada à alguma prática sexual', 'Fui forçada à alguma prática sexual'),
        ('Fui empurrada', 'Fui empurrada'),
        ('Não estou sofrendo nenhum tipo de violência', 'Não estou sofrendo nenhum tipo de violência'),
    )

    types_of_violence = forms.MultipleChoiceField(
        choices=violence,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep4(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Você está em atendimento psicológico e/ou jurídico fora do Mapa do Acolhimento?"
    violence = (
        ('Não estou sendo acompanhada', 'Não estou sendo acompanhada'),
        ('Estou sendo acompanhada por um(a) psicólogo(a) particular', 'Estou sendo acompanhada por um(a) psicólogo(a) particular'),
        ('Estou sendo acompanhada por um(a) advogado(a) particular', 'Estou sendo acompanhada por um(a) advogado(a) particular'),
        ('Estou sendo acompanhada na defensoria pública/ NUDEM', 'Estou sendo acompanhada na defensoria pública/ NUDEM'),
    )

    types_of_violence = forms.MultipleChoiceField(
        choices=violence,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep5(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Defina qual valor corresponde a sua renda individual:"

class MsrStep6(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Qual a sua situação de trabalho?"

    options = (
        ('Empregada com CLT', 'Empregada com CLT'),
        ('Empregada sem CLT', 'Empregada sem CLT'),
        ('Desempregada', 'Desempregada'),
        ('Empreendedora autônoma', 'Empreendedora autônoma'),
        ('Estudante e com renda independente', 'Estudante e com renda independente'),
        ('Aposentada', 'Aposentada'),
        ('Estudante e dependente da minha família', 'Estudante e dependente da minha família'),

    )

    has_dependents = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep7(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Você tem dependentes financeiros?"

    options = (
        ('Sim, eu tenho', 'Sim, eu tenho'),
        ('Não, eu não tenho', 'Não, eu não tenho'),
    )

    financially_dependent = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep8(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = 'Você é responsável financeiramente pela renda familiar ("chefe de família")?'

    options = (
        ('Sim, eu sou', 'Sim, eu sou'),
        ('Não, eu não sou', 'Não, eu não sou'),
    )

    financially_responsible = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep9(forms.Form):
    titulo = "Sobre sua renda"
    subtitulo = "Você possui bens móveis e/ou bens imóveis em seu nome?"
    options = (
        ('Sim, eu tenho', 'Sim, eu tenho'),
        ('Não, eu não tenho', 'Não, eu não tenho'),
    )

    properties = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

    options = (
        ('Sim, eu tenho', 'Sim, eu tenho'),
        ('Não, eu não tenho', 'Não, eu não tenho'),
    )

    properties = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),  # Adicione classes do Tailwind CSS aqui
    )

class MsrStep10(forms.Form):
    titulo = "Formulário finalizado com sucesso"
    subtitulo = "Nesse momento estamos verificando seus dados"

class MsrStep11(forms.Form):
    titulo = "Você não está sozinha"
    subtitulo = "Com base nas suas respostas identificamos que você pode ser atendida pelo projeto. Agora precisamos de mais algumas informações para concluir o seu cadastro e te direcionar para o atendimento adequado. Vamos lá?"