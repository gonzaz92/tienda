from django.urls import path
from tienda.views import index

urlpatterns = [
    path('', index, name='index'),
]