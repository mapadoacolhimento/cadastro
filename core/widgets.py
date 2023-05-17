from django import forms


class InputDaisyUI:
    classnames = "input input-bordered w-full max-w-xs"

    def build_classnames(self, base_attrs, extra_attrs=None):
        """Build an attribute dictionary."""
        return {"class": self.classnames, **base_attrs, **(extra_attrs or {})}


class ValidateOnBlur:

    def build_validate(self, base_attrs, extra_attrs=None):
        attrs = {**base_attrs, **(extra_attrs or {})} 

        if self.is_required:
            attrs.update({"data-validate-required": ""})
        
        if self.input_type == 'email':
            attrs.update({"data-validate-email": ""})

        return attrs
    


class MyInputMonster(InputDaisyUI, ValidateOnBlur):

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = {**base_attrs, **(extra_attrs or {})}
        
        attrs = self.build_classnames(attrs)
        
        attrs = self.build_validate(attrs)
        
        return attrs


class TextInput(MyInputMonster, forms.TextInput):
    pass


class EmailInput(MyInputMonster, forms.EmailInput):
    pass
