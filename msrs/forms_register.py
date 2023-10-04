from django import forms

class RegisterStep0(forms.Form):
    titulo = "Você não está sozinha"
    subtitulo = "Com base nas suas respostas identificamos que você pode ser atendida pelo projeto. Agora precisamos de mais algumas informações para concluir o seu cadastro e te direcionar para o atendimento adequado. Vamos lá?"

class RegisterStep1(forms.Form):
    titulo = "Seus dados"
    subtitulo = ""

class RegisterStep2(forms.Form):
    titulo = "Seus dados"
    subtitulo = ""

class RegisterStep3(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = ""

class RegisterStep4(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = ""

class RegisterStep5(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = ""

class RegisterStep6(forms.Form):
    titulo = "Sobre a violência"
    subtitulo = ""

class RegisterStep7(forms.Form):
    titulo = "Sobre o acolhimento"
    subtitulo = ""

class RegisterStep8(forms.Form):
    titulo = "Sobre o acolhimento"
    subtitulo = ""

class RegisterStep9(forms.Form):
    titulo = "Cadastro realizado com sucesso"
    subtitulo = ""
