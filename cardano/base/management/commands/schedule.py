import schedule
import time

from django.conf import settings
from django.core.management.base import BaseCommand
from product_details import product_details

from cardano.base.mozillians import MozilliansClient
from cardano.base.models import Mozillian, Country


def _fetch_mozillians():
    mozillians_client = MozilliansClient(settings.MOZILLIANS_API_URL,
                                         settings.MOZILLIANS_API_KEY)

    vouched = mozillians_client.get_users(params={'is_vouched': True})['count']
    total = mozillians_client.get_users()['count']
    Mozillian.objects.create(vouched=vouched, total=total)


def _fetch_countries():
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


class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule.every().week.do(_fetch_mozillians)
        schedule.every().week.do(_fetch_countries)

        while True:
            schedule.run_pending()
            time.sleep(3600)
