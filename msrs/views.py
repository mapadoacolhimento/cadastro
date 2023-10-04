# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import FormDataMsr
from django.views import View
from .forms import MsrStep0, MsrStep1, MsrStep2, MsrStep3, MsrStep4, MsrStep5, MsrStep6, MsrStep7, MsrStep8, MsrStep9, MsrStep10, MsrStep10, MsrStep11
from .forms_register import RegisterStep0, RegisterStep1, RegisterStep2, RegisterStep3, RegisterStep4, RegisterStep5, RegisterStep6, RegisterStep7, RegisterStep8, RegisterStep9

from django.shortcuts import render, redirect

def main(request):
  template = loader.get_template('msrs/forms/screening_home.html')
  return HttpResponse(template.render())

# Wizard Form
class FormWizardView(View):
    template_name = 'msrs/forms/screening_form.html'
    form_classes = [MsrStep0, MsrStep1, MsrStep2, MsrStep3, MsrStep4, MsrStep5, MsrStep6, MsrStep7, MsrStep8, MsrStep9, MsrStep10, MsrStep11]

    def get(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class()

        titulo = form.titulo
        subtitulo = form.subtitulo

        return render(request, self.template_name, {'form': form, 'step': step, 'titulo': titulo, 'subtitulo': subtitulo})

    def post(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class(request.POST)
        if form.is_valid():
            # Armazenando dados do formulário em algum lugar
            # Avançar para a próxima etapa
            # Usando sessão:
            form_data = form.cleaned_data

            # TODO: Passar pro value
            if 'form_data' not in request.session:
                request.session['form_data'] = {}
            request.session['form_data'].update(form_data)
            request.session.modified = True

            if step <= 9:
                return redirect('screening_form', step=step + 1)
            else:
                return redirect('register_form', step=0) #consertar transição de formulário

        return render(request, self.template_name, {'form': form, 'step': step})

class RegisterFormView(View):
    template_name = 'msrs/forms/register_form.html'
    form_classes = [RegisterStep0, RegisterStep1, RegisterStep2, RegisterStep3, RegisterStep4, RegisterStep5, RegisterStep6, RegisterStep7, RegisterStep8, RegisterStep9]

    def get(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class()

        titulo = form.titulo
        subtitulo = form.subtitulo

        return render(request, self.template_name, {'form': form, 'step': step, 'titulo': titulo, 'subtitulo': subtitulo})

    def post(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class(request.POST)
        if form.is_valid():
            # Armazenando dados do formulário em algum lugar
            # Avançar para a próxima etapa
            # Usando sessão:
            form_data = form.cleaned_data

            if 'form_data' not in request.session:
                request.session['form_data'] = {}
            request.session['form_data'].update(form_data)
            request.session.modified = True

            if step <= 8: #Consertar lógica final
                return redirect('register_form', step=step + 1)

        return render(request, self.template_name, {'form': form, 'step': step})
