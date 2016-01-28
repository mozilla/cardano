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
