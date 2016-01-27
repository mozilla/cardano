from celery import task
from django.conf import settings
from product_details import product_details

from cardano.base.mozillians import MozilliansClient
from cardano.base.models import Mozillian, Country


@task
def fetch_mozillians():
    mozillians_client = MozilliansClient(settings.MOZILLIANS_API_URL,
                                         settings.MOZILLIANS_API_KEY)
    vouched = mozillians_client.get_users(params={'is_vouched': True})['count']
    total = mozillians_client.get_users()['count']
    Mozillian.objects.create(vouched=vouched, total=total)


@task
def fetch_countries():
    mozillians_client = MozilliansClient(settings.MOZILLIANS_API_URL,
                                         settings.MOZILLIANS_API_KEY)
    countries = sorted(product_details.get_regions('en-US').values())

    for country in countries:
        vouched = mozillians_client.get_users(
            params={
                'is_vouched': True,
                'country': country
            })['count']
        total = mozillians_client.get_users(
            params={
                'country': country
            })['count']
        Country.objects.create(name=country, vouched=vouched, total=total)
