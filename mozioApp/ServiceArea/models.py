# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class date(models.Model):
	created_at = models.DateTimeField(db_index=True,auto_now=True)
	
	class Meta:
		abstract = True

class Provider(date):
	name = models.TextField()
	email = models.TextField()
	phone = models.TextField()
	language = models.TextField()

	
class Area(date):
	latitude=models.DecimalField(max_digits=9, decimal_places=6)
	longitude=models.DecimalField(max_digits=9, decimal_places=6)
	currency = models.TextField()


class ProviderArea(date):
	provider_id = models.ForeignKey(Provider, related_name='providerArea_provider_id', on_delete=models.PROTECT)
	area_id = models.ForeignKey(Area, related_name='providerArea_area_id', on_delete=models.PROTECT)