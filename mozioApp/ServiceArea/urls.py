from django.conf.urls import url, include
from ServiceArea import views

urlpatterns = [

	url(r'^provider$', views.Services_Providers.as_view()),
	]