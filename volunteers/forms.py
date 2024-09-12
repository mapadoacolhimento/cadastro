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
    
    def clean_email(self):
        return self.cleaned_data['email'].lower()
    
    def clean_first_name(self): 
        return self.cleaned_data["first_name"].title()
    
    def clean_last_name(self): 
        return self.cleaned_data["last_name"].title()   