from django.shortcuts import render

from cardano.base.models import Mozillian, Country


def index(request):
    try:
        mozillians = Mozillian.objects.latest()
    except Mozillian.DoesNotExist:
        return render(request, 'home.html')
    countries = Country.objects.order_by('name', '-created').distinct('name')

    vouched_diff = 0
    total_diff = 0
    if Mozillian.objects.count() > 1:
        previous_week = mozillians.get_previous_by_created()
        vouched_diff = mozillians.vouched - previous_week.vouched
        total_diff = mozillians.total - previous_week.total

    countries_diff = []
    for country in countries:
        country_vouched_diff = 0
        country_total_diff = 0
        if Country.objects.filter(name=country.name).count() > 1:
            previous_week = Country.objects.filter(name=country.name)[1]
            country_vouched_diff = country.vouched - previous_week.vouched
            country_total_diff = country.total - previous_week.total
        country_diff = {
            'name': country.name,
            'vouched_diff': country_vouched_diff,
            'total_diff': country_total_diff
        }
        countries_diff.append(country_diff)

    return render(request, 'home.html', {'countries': countries,
                                         'mozillians': mozillians,
                                         'vouched_diff': vouched_diff,
                                         'total_diff': total_diff,
                                         'countries_diff': countries_diff})
