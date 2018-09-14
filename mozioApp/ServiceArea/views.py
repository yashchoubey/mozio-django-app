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


class Update_Service_Area(APIView):
	def post(self,request):
		providerObj = provider.objects.get(id=request.data['id'])
		providerObj.service_area=data['service_area']
		providerObj.save()
	
	def get(self,request):
		providerObj = provider.objects.get(id=request.data['id'])
		return Response(json.dumps(provider.service_area), status=200)

    try:
        provider = Provider.objects.get(pk=id)
        
        if request.method == "POST":
            provider.service_area = []
            for poly in data['service_area']:
                provider.service_area.append(poly)
            provider.save()
            return json_response(provider.to_json(), 201)

        elif request.method == "PUT":
            for poly in data['service_area']:
                provider.service_area.append(poly)
            provider.save()
            return json_response(provider.to_json(), 200)
        elif request.method == "DELETE":
            for poly in data['service_area']:
                poly = {"type":"Polygon","coordinates":poly}
                if poly in provider.service_area:
                    provider.service_area.remove(poly)
            provider.save()
            return json_response(provider.to_json(), 200)
        else:
            raise MethodError("Allowed Method: POST,PUT,DELETE")
    except Exception as e:
        return error_handler(e)


@cache_page(60 * 15)        #Cache response in Redis for 15 minutes
@csrf_exempt
def search(request):
    try:
        if request.method == "GET":
            lat = request.GET.get("lat")
            long = request.GET.get("long")
            providers = Provider.objects(__raw__={
                            "service_area": {
                                    "$geoIntersects": {
                                        "$geometry": {
                                          "type": "Point" ,
                                          "coordinates": [float(lat), float(long)]
                                        }

                                    }}})
            return json_response(providers.to_json(),200)
        else:
            response = dict()
            response['error'] = "Allowed Methods: GET"
            return json_response(json.dumps(response),400)
    except Exception as e:
        return error_handler(e)