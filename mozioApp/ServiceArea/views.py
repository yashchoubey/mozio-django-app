# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from ServiceArea.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.shortcuts import render
# Create your views here.

class Services_Providers(APIView):
	def get(self,request):
		providerObjects=Provider.objects.all()
		return Response([{
			'name' : x.name,
			'email' : x.email,
			'phone' : x.phone,
			'language' : x.language,
			# 'currency' : x.currency
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
			language = request.data['language'],
			# currency = request.data['currency']
		)
		return Response(status=200)


class Update_Service_Area(APIView):
	def post(self,request):
		providerObj = Provider.objects.get(id=request.data['id'])
		providerObj.service_area=data['service_area']
		providerObj.save()
	
	def get(self,request):
		providerObj = Provider.objects.get(id=request.data['id'])
		return Response(json.dumps(provider.service_area), status=200)

	