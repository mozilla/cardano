from django.contrib import admin

from cardano.base.models import Mozillian, Country


@admin.register(Mozillian)
class MozillianAdmin(admin.ModelAdmin):
    list_display = ('vouched', 'total', 'created')
    readonly_fields = ('vouched', 'total', 'created')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('vouched', 'total', 'name', 'created')
    readonly_fields = ('vouched', 'total', 'name', 'created')
