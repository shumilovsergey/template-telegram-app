from django.urls import path
from .views import Main
from .views import Out



app_name = 'api'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('out', Out.as_view(), name='out')
]