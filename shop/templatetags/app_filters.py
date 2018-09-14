from django import template

register = template.Library()


# @register.filter(name='range')
def times(n):
    return range(n)


register.filter('range', times)
