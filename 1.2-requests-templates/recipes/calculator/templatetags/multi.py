from django import template
register = template.Library()


@register.filter
def multi(a, b):
    return a * b
