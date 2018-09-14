# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from ServiceArea.models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class Services_Providers(APIView):
	def get(self,request):
		providerObjects=Provider.objects.all()
		return Response([{
			'name' : x.name,
			'email' : x.email,
			'phone' : x.phone,
			'language' : x.language,
		} for x in providerObjects],status=200)

	def put(self,request):
		providerObject=Provider.objects.get(id=request.data['id'])
		for key in request.data.keys():
			providerObject.key=request.data[key]

		providerObject.save()
		return Response(status=200)
	
	def delete(self,request):
		providerObject=Provider.objects.get(id=request.data['id'])
		providerObject.delete()
		return Response(status=200)
	
	def post(self,request):
		providerObject=Provider.objects.get_or_create(
			name = request.data['name'],
			email = request.data['email'],
			phone = request.data['phone'],
			language = request.data['language']
		)
		return Response(status=200)


class Update_Service_Area(APIView):
	#Method to make a new entry
	def post(self,request):
		providerObj = Provider.objects.get(id=request.data['id'])
		areaObj = Area.objects.get_or_create(latitude=request.data['latitude'],longitude=request.data['longitude'],currency=request.data['currency'])[0]
		providerAreaObj = ProviderArea.objects.get_or_create(provider_id=providerObj,area_id=areaObj)
		return Response(status=200)

	#Method to fetch all service areas for existing provider
	def get(self,request):
		providerObj = Provider.objects.get(id=request.data['id'])
		providerAreaObjs = ProviderArea.objects.filter(provider_id=providerObj)
		return Response([{
			'latitude':x.latitude,
			'longitude':x.longitude,
			'currency':x.currency
		} for x in providerAreaObjs ], status=200)

	