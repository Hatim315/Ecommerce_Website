from django import template
register=template.Library()
@register.filter
def index(m,n):
    i=n
    return m[i]