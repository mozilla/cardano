from django.shortcuts import render

from cardano.base.models import Mozillian, Country


def index(request):
    countries = Country.objects.order_by('name', '-created').distinct('name')
    mozillians = Mozillian.objects.latest()

    previous_week = Mozillian.objects.order_by('-created')[1]
    vouched_diff = mozillians.vouched - previous_week.vouched
    total_diff = mozillians.total - previous_week.total

    countries_diff = []
    for country in countries:
        previous_week = Country.objects.filter(name=country.name)[1]
        country_diff = {
            'name': country.name,
            'vouched_diff': country.vouched - previous_week.vouched,
            'total_diff': country.total - previous_week.total
        }
        countries_diff.append(country_diff)

    return render(request, 'home.html', {'countries': countries,
                                         'mozillians': mozillians,
                                         'vouched_diff': vouched_diff,
                                         'total_diff': total_diff,
                                         'countries_diff': countries_diff})
