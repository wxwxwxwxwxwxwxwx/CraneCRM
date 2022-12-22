
from django.urls import path
from django.contrib import admin
from django.conf import settings 
from . import views

admin.site.site_header = settings.ADMIN_SITE_HEADER
urlpatterns = [
    path('', views.index, name = 'index'),
    path('Document', views.upload, name='Document'),
    path('getaddressfromphone', views.get_address_from_phone, name='getaddressfromphone')
]    
 



