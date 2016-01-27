from django.shortcuts import render

from cardano.base.models import Mozillian, Country


def index(request):
    countries = Country.objects.order_by('name').distinct('name')
    mozillians = Mozillian.objects.latest()

    return render(request, 'home.html', {'countries': countries,
                                         'mozillians': mozillians})
