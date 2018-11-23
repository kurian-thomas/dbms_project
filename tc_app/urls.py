from django.conf.urls import url,include
from django.contrib import admin
from tc_app import views 

app_name = 'tc_app'

urlpatterns = [
	url(r'^testpage/', views.test, name='test'),
	url(r'^get_element_log/', views.get_element_log, name='get_login'),
	url(r'^index/', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^get_element/', views.get_element, name='get_element'),
	url(r'^test/(?P<test_number>[0-9]+)/', views.test, name='test'),
	url(r'^test/', views.test, name='test'),
	url(r'^logout/', views.logout, name='logout'),
]
