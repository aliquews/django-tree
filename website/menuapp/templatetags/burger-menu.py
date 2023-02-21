from django import template
from django.http import HttpRequest

from menuapp.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: template.RequestContext, menu_name, parent_id=None):
    current_path = context['request'].path if 'request' in context and isinstance(context['request'], HttpRequest) else ''
    if menu_name == 'root':
        items = MenuItem.objects.filter(parent__name='-')
    items = MenuItem.objects.filter(parent=parent_id)
    
    print(items)

    for item in items:
       item.active = item.url == current_path
       if not item.active:
           item.active = current_path.startswith(item.url) if item.url.endswith('/') else current_path.startswith(item.url+'/')
    return {'current_menu': items, 'name': menu_name}