from django import template

register = template.Library()


@register.filter(name='short_name')
def short_name(value):
    return f'{value.split()[0][0]}{value.split()[1][0]} {value.split()[-1]}'
