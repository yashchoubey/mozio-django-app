# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.
class Provider(APIView):
	def get(self,request):
		providerObjects=provider.objects.all()
		return Response([{
			'name' = x.name,
			'email' = x.email,
			'phone' = x.phone,
			'language' = x.language,
			'currency' = x.currency
		} for x in providerObjects],status=200)

	
	def put(self,request):
		providerObject=provider.objects.get(id=request.data['id'])
		for key in request.data.keys():
			providerObject.key=request.data[key]

		providerObject.save()
		return Response(status=200)

	
	def delete(self,request):
		providerObject=provider.objects.get(id=request.data['id'])
		providerObject.delete()
		return Response(status=200)
	
	def post(self,request):
		providerObject=provider.objects.get_or_create(
			name = request.data['name'],
			email = request.data['email'],
			phone = request.data['phone'],
			language = request.data['language'],
			currency = request.data['currency']
		)

		return Response(status=200)