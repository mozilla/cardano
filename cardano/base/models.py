from django.db import models


class Mozillian(models.Model):
    vouched = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'


class Country(models.Model):
    vouched = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    name = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'
