from django import template

register = template.Library()

@register.filter(name='Censor')
def Censor1(value,arg):
    value = value.replace("ненормативная", "***")
    value = value.replace("обзывается", "***")
    value = value.replace("ругательство", "***")
    return value