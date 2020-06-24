from django.urls import path

from . import views

urlpatterns = [
    path('', views.index) # empty route redirect to index function in views file

]
