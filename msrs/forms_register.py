from django import forms
from volunteers.fields import CharField, TextField, EmailField, ChoiceField, SelectField


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
        choices=(
            ("ss", "Estado"),
            ("sp", "São Paulo"),
            ("rj", "Rio de Janeiro"),
            ("mg", "Minas Gerais"),
        ),
    )

    city = SelectField(
        label="Cidade",
        choices=(("ss", "Cidade"), ("rio", "Rio de Janeiro"), ("bh", "Belo Horizonte")),
    )

    # Campo de texto para o bairro
    neighborhood = CharField(label="Bairro", max_length=100)


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
    titulo = "Sobre a violência"
    subtitulo = ""

    author_violence = SelectField(
        label="Quem é ou foi o(a) autor(a) da violência?",
        choices=(("1", "1"), ("1", "1")),
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
    titulo = "Sobre a violência"
    subtitulo = "Selecione as opções de fatores de risco que se aplicam ao seu caso:"
    options = (
        (
            "O(A) autor(a) da violência possui acesso à arma de fogo",
            "O(A) autor(a) da violência possui acesso à arma de fogo",
        ),
        ("Ocorreu em ambiente doméstico", "Ocorreu em ambiente doméstico"),
        ("Não me sinto segura em casa", "Não me sinto segura em casa"),
        ("Estou em cárcere privado", "Estou em cárcere privado"),
        (
            "Ocorreu em ambiente público (internet, rua, etc)",
            "Ocorreu em ambiente público (internet, rua, etc)",
        ),
        ("Ocorreu em ambiente de trabalho", "Ocorreu em ambiente de trabalho"),
        (
            "O(A) autor(a) tem diagnóstico de doença psiquiátrica",
            "O(A) autor(a) tem diagnóstico de doença psiquiátrica",
        ),
        (
            "O(A) autor(a) faz uso de substância psicoativa",
            "O(A) autor(a) faz uso de substância psicoativa",
        ),
        (
            "Dependo financeiramente do(a) autor(a) da violência",
            "Dependo financeiramente do(a) autor(a) da violência",
        ),
        (
            "Tive acesso negado aos serviços públicos de atendimento à mulher",
            "Tive acesso negado aos serviços públicos de atendimento à mulher",
        ),
        (
            "As agressões ou ameaças do(a) autor(a) da violência contra mim se ",
            "tornaram mais frequentes ou mais graves nos últimos meses",
        ),
    )

    risk_factor = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class RegisterStep5(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Selecione as opções de fatores de proteção que se aplicam ao seu caso:"
    options = (
        (
            "Eu possuo rede de apoio (familiares, amigos, vizinhos etc)",
            "Eu possuo rede de apoio (familiares, amigos, vizinhos etc)",
        ),
        (
            "Não resido com o(a) autor(a) da violência",
            "Não resido com o(a) autor(a) da violência",
        ),
        ("Não me sinto segura em casa", "Não me sinto segura em casa"),
        ("Me sinto segura em casa", "Me sinto segura em casa"),
        (
            "Não dependo financeiramente do(a) autor(a) da violência",
            "Não dependo financeiramente do(a) autor(a) da violência",
        ),
        (
            "O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado",
            "O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado",
        ),
    )

    protection_factor = forms.MultipleChoiceField(
        choices=options,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "custom-checkbox"}),
    )


class RegisterStep6(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = "Você está sendo atendida por algum serviço da rede de atendimento de violência contra as mulheres da região e ou por algum coletivo/ movimento?"

    options = [
        ("Sim, eu estou sendo atendida", "Sim, eu estou sendo atendida"),
        ("Não, eu não estou sendo atendida", "Não, eu não estou sendo atendida"),
    ]

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
