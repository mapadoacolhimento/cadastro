from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def render_progress_items(total, activate_index):
    items = ""
    
    for x in range(total):
        if x <= activate_index:
            items += '<li class="my-step my-step-active"></li>'
        else:
            items += '<li class="my-step"></li>'

    return mark_safe(items)