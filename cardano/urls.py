from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from cardano.base import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
    ]
