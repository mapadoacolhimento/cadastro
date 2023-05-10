from django.forms.renderers import TemplatesSetting


class DaisyUIFormRenderer(TemplatesSetting):
    form_template_name = 'daisyui/form.html'
