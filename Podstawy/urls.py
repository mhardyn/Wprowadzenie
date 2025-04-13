from django.urls import path # funkcja ścieżki
from . import views

urlpatterns = [
    path('hello-world', views.hello_world), # funkcję przekazujemy bez nawiasów
    path('current-time', views.current_time),
    path('count', views.count),
    path('country/<str:country_name>', views.country_by_name),
]

