from django.urls import path

from shop.views import hello

urlpatterns = [
    path('', hello),
]