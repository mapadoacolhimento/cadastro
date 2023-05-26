from typing import Any, Optional, Sequence, Type, Union
from django import forms
from django.forms.widgets import Widget
from django.core.validators import RegexValidator, MinLengthValidator


class OverridePlaceholderLabel:

    def widget_attrs(self, widget):
        attrs = super(OverridePlaceholderLabel, self).widget_attrs(widget)

        attrs.update({"placeholder": self.label})
        attrs.update({self.label: ""})

        return attrs


class TextField(OverridePlaceholderLabel, forms.TextInput):
    widget = forms.Textarea


class CharField(OverridePlaceholderLabel, forms.CharField):
    widget = forms.TextInput


class EmailField(OverridePlaceholderLabel, forms.EmailField):
    widget = forms.EmailInput


class ChoiceField(OverridePlaceholderLabel, forms.ChoiceField):
    pass


class MaskField(OverridePlaceholderLabel, forms.CharField):
    widget = forms.TextInput

    def __init__(self, mask, **kwargs) -> None:
        self.mask = mask
        super(MaskField, self).__init__(**kwargs)

    def widget_attrs(self, widget):
        attrs = super(MaskField, self).widget_attrs(widget)

        attrs.update({"data-mask": self.mask},
                     validators=[MinLengthValidator(self.min_length)])

        return attrs


class ZipCodeField(MaskField):
    widget = forms.TextInput
    max_length = 9
    default_validators = [RegexValidator(regex=r"^[0-9]{5}-[0-9]{3}$")]

    def widget_attrs(self, widget):
        attrs = super(ZipCodeField, self).widget_attrs(widget)

        attrs.update({"data-validate-zipcode": ""})

        return attrs
