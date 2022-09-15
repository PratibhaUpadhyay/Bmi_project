
from django.urls import path
from .views import home

urlpatterns = [  
    path('', include, name='home')
]
