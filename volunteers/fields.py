from typing import Any, Optional, Sequence, Type, Union
from django import forms
from django.forms.widgets import Widget
from django.core.validators import RegexValidator, MinLengthValidator


class OverridePlaceholderLabel:
    def widget_attrs(self, widget):
        attrs = super(OverridePlaceholderLabel, self).widget_attrs(widget)
        attrs.update({"placeholder": " "})
        attrs["class"] = "peer"

        return attrs


class TextField(OverridePlaceholderLabel, forms.TextInput):
    widget = forms.Textarea


class CharField(OverridePlaceholderLabel, forms.CharField):
    widget = forms.TextInput


class EmailField(OverridePlaceholderLabel, forms.EmailField):
    widget = forms.EmailInput
    default_error_messages = {"invalid": "Digite um e-mail válido"}


class ChoiceField(OverridePlaceholderLabel, forms.ChoiceField):
    pass


class SelectField(OverridePlaceholderLabel, forms.ChoiceField):
    widget = forms.Select

    def widget_attrs(self, widget):
        attrs = super(SelectField, self).widget_attrs(widget)
        attrs.update({"onchange": "hideSelectLabel(this.value, this.name);"})
        return attrs


class CustomLogicField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        return None


class MaskField(OverridePlaceholderLabel, forms.CharField):
    widget = forms.TextInput

    def __init__(self, mask, **kwargs) -> None:
        self.mask = mask
        super(MaskField, self).__init__(**kwargs)

    def widget_attrs(self, widget):
        attrs = super(MaskField, self).widget_attrs(widget)

        attrs.update(
            {"data-mask": self.mask}, validators=[MinLengthValidator(self.min_length)]
        )

        return attrs


class ZipCodeField(MaskField):
    widget = forms.TextInput
    default_validators = [RegexValidator(regex=r"^[0-9]{5}-[0-9]{3}$")]
    default_error_messages = {"invalid": "Digite um CEP válido"}

    def widget_attrs(self, widget):
        attrs = super(ZipCodeField, self).widget_attrs(widget)

        attrs.update({"data-validate-zipcode": ""})

        return attrs


class DateField(OverridePlaceholderLabel, forms.DateField):
    default_error_messages = {"invalid": "Digite uma data válida"}

    widget = forms.DateInput(
        format="%d-%m-%Y",
        attrs={
            "class": "date",
        },
    )
    input_formats = ["%d/%m/%Y", "%Y-%m-%d"]

    def widget_attrs(self, widget):
        attrs = super(DateField, self).widget_attrs(widget)
        attrs.update({"data-mask": "00/00/0000"})
        return attrs
