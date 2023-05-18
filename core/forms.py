from django import forms


def unzip_widget(label, Widget=forms.TextInput, **extra_attrs):
    if not extra_attrs:
        extra_attrs = dict()

    extra_widget_attrs = extra_attrs.pop('widget_attrs', None)

    widget = Widget(
        attrs={"class": "input input-bordered w-full max-w-xs", "placeholder": label})

    if extra_widget_attrs:
        widget = Widget(
            attrs={"class": "input input-bordered w-full max-w-xs",
                   "placeholder": label},
            **extra_widget_attrs
        )

    extra_attrs.update({
        "label": label,
        "widget": widget
    })

    return extra_attrs


class PeopleForm(forms.Form):
    first_name = forms.CharField(
        **unzip_widget("Primeiro nome")
    )
    last_name = forms.CharField(**unzip_widget("Sobrenome", required=False))
    email = forms.EmailField(
        **unzip_widget("Seu melhor e-mail", widget=forms.EmailInput))
    phone_number = forms.CharField(**unzip_widget("Número de telefone"))
    document_number = forms.CharField(**unzip_widget("CRP"))

    template_name = "forms/daisyui.html"


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
    color = forms.CharField(
        **unzip_widget("Cor", Widget=forms.Select, widget_attrs={"choices": COLOR_CHOICES})
    )
    gender = forms.CharField(
        **unzip_widget("Identidade de gênero", Widget=forms.Select, widget_attrs={"choices": GENDER_CHOICES})
    )
    zipcode = forms.CharField(**unzip_widget("CEP de atendimento"))
    phone = forms.CharField(**unzip_widget("Telefone de atendimento com DDD"))

    template_name = "forms/daisyui.html"
