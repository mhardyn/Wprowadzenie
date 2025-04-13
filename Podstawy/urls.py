from django.urls import path  # funkcja ścieżki
from . import views

urlpatterns = [
    path('hello-world', views.hello_world),  # funkcję przekazujemy bez nawiasów
    path('current-time', views.current_time),
    path('count', views.count),
    path('country/<int:country_index>', views.country_by_index),
    path('country/<str:country_name>', views.country_by_name, name='country_by_name_url'),
    path('first-html', views.first_html),
    path('country-list/<int:count>', views.country_list, name='country_list_url'),
    path('first-template', views.first_template),
]
