from django.contrib import admin
from django.urls import path

#added manually
from controlpanel import views

urlpatterns = [
   path("",views.index,name='Home'),
   path("files",views.files,name='My files'),
   path("more",views.more,name='More'),
   path("controlpanel",views.controlpanel,name='Control Panel')

]
