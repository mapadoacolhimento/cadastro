from django import forms

# from .fields import CharField, ChoiceField, EmailField, MaskField, ZipCodeField

from django.contrib.auth.models import User


# TODO: replace Form with ModelForm
class VolunteerForm(forms.Form):
    template_name = "volunteers/forms/daisyui-form.html"

    def __init__(self, fields=[], *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        self.fields = fields
        for field in self.fields.values():
            field.error_messages["required"] = "Preencha este campo"
