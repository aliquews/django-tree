from django import template
from django.http import HttpRequest
from django.urls import reverse

from menuapp.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: template.RequestContext, menu_name: str | None = None, parent_id: int | None = None):
    current_path = context['request'].path if 'request' in context and isinstance(context['request'], HttpRequest) else ''
    if menu_name is None:
        items = MenuItem.objects.filter(parent__name='-')
    items = MenuItem.objects.filter(parent=parent_id)
    for item in items:
        try:
            item.url = reverse(item.url)
        except:
            pass
        item.active = item.url == current_path
        if not item.active:
           item.active = current_path.startswith(item.url) if item.url.endswith('/') else current_path.startswith(item.url+'/')
    return {'current_menu': items, 'name': menu_name}