from django import forms


class ValidateOnBlur:

    def build_validate(self, base_attrs, extra_attrs=None):
        attrs = {**base_attrs, **(extra_attrs or {})}

        if self.is_required:
            attrs.update({"data-validate-required": ""})

        if self.input_type == 'email':
            attrs.update({"data-validate-email": ""})

        return attrs


class MyInputMonster(ValidateOnBlur):

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = {**base_attrs, **(extra_attrs or {})}

        attrs = self.build_validate(attrs)

        return attrs


class TextInput(MyInputMonster, forms.TextInput):
    pass


class EmailInput(MyInputMonster, forms.EmailInput):
    pass
