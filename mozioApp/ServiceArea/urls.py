from django.conf.urls import url, include
from ServiceArea import views

urlpatterns = [

	url(r'^provider$', views.Provider.as_view()),
	]