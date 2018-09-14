# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from djgeojson.fields import PointField
# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class date(models.Model):
	created_at = models.DateTimeField(db_index=True,auto_now=True)
	# updated_at= models.DateTimeField(db_index=True,default=None, blank=True, null=True)
	
	class Meta:
		abstract = True

class provider(date):
	name = models.TextField()
	email = models.TextField()
	phone = models.TextField()
	language = models.TextField()
	currency = models.TextField()
	# created_at = models.DateTimeField(auto_now=True)

	
class area(date):
	service_area = models.PolygonField()
	currency = models.TextField()
	# created_at = models.DateTimeField(db_index=True,auto_now=True)


class providerArea(date):
	provider_id = models.ForeignKey(provider, related_name='providerArea_provider_id', on_delete=models.PROTECT,)
	area_id = models.ForeignKey(area, related_name='providerArea_area_id', on_delete=models.PROTECT,)
	
	
# class area(date):
# 	geom = PointField()
# 	