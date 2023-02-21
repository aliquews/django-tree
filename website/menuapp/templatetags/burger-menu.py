from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(request, context):
    pass