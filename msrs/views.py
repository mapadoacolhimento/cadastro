# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# from .models import FormDataMsr
from django.views import View
from formtools.wizard.views import SessionWizardView
from .forms import (
    MsrStep0,
    MsrStep1,
    MsrStep2,
    MsrStep3,
    MsrStep4,
    MsrStep5,
    MsrStep6,
    MsrStep7,
    MsrStep8,
    MsrStep9,
)
from .forms_register import (
    RegisterStep0,
    RegisterStep1,
    RegisterStep2,
    RegisterStep3,
    RegisterStep4,
    RegisterStep5,
    RegisterStep6,
    RegisterStep7,
    RegisterStep8,
    RegisterStep9,
)

from django.shortcuts import render, redirect
from django.db import transaction

from .models import FormData


def main(request):
    template = loader.get_template("msrs/forms/screening_home.html")
    return HttpResponse(template.render())


# Wizard Form

class FormWizardView(SessionWizardView):
    template_name = "msrs/forms/screening_wizard_form.html"
    form_list = [
        MsrStep0,
        MsrStep1,
        MsrStep2,
        MsrStep3,
        MsrStep4,
        MsrStep5,
        MsrStep6,
        MsrStep7,
        MsrStep8,
        MsrStep9,
    
    ]
    
    def process_step(self, form):
      return self.get_form_step_data(form)

# class FormWizardView(View):
#     template_name = "msrs/forms/screening_form.html"
#     form_classes = [
#         MsrStep0,
#         MsrStep1,
#         MsrStep2,
#         MsrStep3,
#         MsrStep4,
#         MsrStep5,
#         MsrStep6,
#         MsrStep7,
#         MsrStep8,
#         MsrStep9,
    
#     ]

#     def get(self, request, step=0, *args, **kwargs):
#         form_class = self.form_classes[step]
#         form = form_class()

#         titulo = form.titulo
#         subtitulo = form.subtitulo

#         return render(
#             request,
#             self.template_name,
#             {"form": form, "step": step, "titulo": titulo, "subtitulo": subtitulo},
#         )

#     def post(self, request, step=0, *args, **kwargs):
#         form_class = self.form_classes[step]
#         form = form_class(request.POST)
#         if form.is_valid():
#             # Armazenando dados do formulário em algum lugar
#             # Avançar para a próxima etapa
#             # Usando sessão:
            
#             form_data = form.cleaned_data
#             #import ipdb; ipdb.set_trace()
#             # TODO: Passar pro value
#             if "form_data" not in request.session:
#                 request.session["form_data"] = {}
#             request.session["form_data"].update(form_data)
#             request.session.modified = True
#          #return redirect("screening_form", step=step + 1)
#             if step <= 8:
#                 return redirect("screening_form", step=step + 1)
#             else:
#                 self.done(form_list=self.form_classes)
#         return render(request, self.template_name, {"form": form, "step": step})

    transaction.atomic
    def done(self, form_list, **kwargs):
        values = list(map(lambda form: form.cleaned_data, form_list))
        form_data = FormData.objects.create(values=values)
        return redirect("register_home", form_data_id=form_data.id)


class RegisterFormView(View):
    template_name = "msrs/forms/register_form.html"
    form_classes = [
        RegisterStep0,
        RegisterStep1,
        RegisterStep2,
        RegisterStep3,
        RegisterStep4,
        RegisterStep5,
        RegisterStep6,
        RegisterStep7,
        RegisterStep8,
        RegisterStep9,
    ]

    def get(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class()

        titulo = form.titulo
        subtitulo = form.subtitulo

        return render(
            request,
            self.template_name,
            {"form": form, "step": step, "titulo": titulo, "subtitulo": subtitulo},
        )

    def post(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class(request.POST)
        if form.is_valid():
            # Armazenando dados do formulário em algum lugar
            # Avançar para a próxima etapa
            # Usando sessão:
            form_data = form.cleaned_data

            if "form_data" not in request.session:
                request.session["form_data"] = {}
            request.session["form_data"].update(form_data)
            request.session.modified = True

            if step <= 8:  # Consertar lógica final
                return redirect("register_form", step=step + 1)

        return render(request, self.template_name, {"form": form, "step": step})


def loading(request,form_data_id):
    template = loader.get_template("msrs/forms/screening_load.html")
    return HttpResponse(template.render())


def register_home(request,form_data_id):
    template = loader.get_template("msrs/forms/register_home.html")
    return HttpResponse(template.render())
