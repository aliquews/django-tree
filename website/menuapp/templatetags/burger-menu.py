import re

from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch

from menuapp.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(contest: RequestContext):
    pass