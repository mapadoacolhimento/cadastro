# utils.py
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.http import require_GET
from .models import Place

def loading(request, form_data_id):
    template = loader.get_template("msrs/forms/screening_load.html")
    return HttpResponse(template.render())

def register_home(request, form_data_id):
    template = loader.get_template("msrs/forms/register_home.html")
    return HttpResponse(template.render())

@require_GET
def get_cities_for_state(request):
    state = request.GET.get('state')
    cities = Place.objects.filter(state=state).values('city')
    city_list = [city['city'] for city in cities]
    return JsonResponse({'cities': city_list})
