from django import template

register = template.Library()


@register.filter
def lookup_country_vouched(countries, key):
    q = max(countries, key=lambda d: (d['name'] == key))
    return q['vouched_diff']


@register.filter
def lookup_country_total(countries, key):
    q = max(countries, key=lambda d: (d['name'] == key))
    return q['total_diff']


@register.filter
def glyphicon_type(number):
    if number > 0:
        return 'glyphicon-triangle-top'
    elif number < 0:
        return 'glyphicon-triangle-bottom'
    else:
        return 'glyphicon-minus'
