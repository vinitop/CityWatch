from django.contrib import admin
from django.urls import path
from controlpanel import views

urlpatterns = [
   path("",views.index,name='Control Panel'),
   path("files",views.files,name='My files'),
   path("more",views.more,name='More')
]
