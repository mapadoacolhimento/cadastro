from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def render_progress_items(total, activate_index):
    items = ""

    for x in range(total):
        if x <= activate_index:
            items += '<div class="my-step my-step-active"></div>'
        else:
            items += '<div class="my-step"></div>'

    return mark_safe(items)
