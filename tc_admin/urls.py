from django.conf.urls import url,include
from django.contrib import admin
from tc_admin import views 

app_name = 'tc_admin'

urlpatterns = [
	url(r'^create_test/', views.createtest, name='create_test'),
	url(r'^create_test_form/', views.create_test_form, name='create_test_form'),
	url(r'^get_element_adminlog/', views.adlogin, name='admin_login'),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^login/', views.login, name='login'),
]
