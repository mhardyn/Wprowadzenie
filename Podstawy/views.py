import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import find_by_name, all_countries
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.

counter = 0


def hello_world(request):
    return HttpResponse("Hello World from Django!")


def current_time(request):
    return HttpResponse(f'Czas wywołania widoku: {datetime.datetime.now()}')


# Proszę napisać ścieżkę, która będzie zwracała informacje ile razy została wywołana:
# a. Dodanie mapowania ścieżki URL
# b. Dodanie nowej metody w views.py

# lab 1 django
def count(request):
    global counter
    counter += 1
    return HttpResponse(f'Ilość wywołań: {++counter}')


def country_by_name(request, country_name):
    found_country = find_by_name(country_name)
    if found_country is None:
        return HttpResponseNotFound(f'Nie znaleziono kraju o nazwie {country_name}')
    return render(request, 'podstawy/country.html', {
        'found_country': found_country
    })


def country_by_index(request, country_index):
    if country_index > len(all_countries):
        return HttpResponseNotFound(f'Nie znaleziono kraju o indeksie {country_index}')
    found_country = all_countries[country_index]
    return HttpResponseRedirect(reverse('country_by_name_url', args=[found_country['country']]))


def first_html(request):
    response_data = """
    <h1>To jest HTML</h1>
    <ul>
        <li>jeden</li>
        <li>dwa</li>
        <li>trzy</li>
        <li>cztery</li>
        <li><a href='https://google.com'>Google</a></li>
        <li><a href='http://localhost:8000/basics/country/poland'>Poland</a></li>
    </ul>
    """
    return HttpResponse(response_data)


# 1. Proszę napisać widok, który pobierze od nas maksymalną liczbę krajów w liście i zwróci widok listy krajów jako lista HTML (<ul>,<li>). Każdy z elementów listy powinien być
# hiperłączem i po kliknięciu przenieść do widoku szczegółów kraju (te widoku mamy już napisane. Proszę wykorzystać tag <a> z wartością href).
# a. Dodanie mapowania ścieżki URL ze zmienną dynamiczną przyjmującą liczbę krajów
# do wyświetlenia
# b. Dodanie nowej metody w views.py która zwróci kod HTML jako ciąg znaków

# lab 2
# def country_list(request, count):
#     list_items = ""
#     for country in all_countries[:count]:
#         country_name = country['country']
#         country_path = reverse('country_by_name_url', args=[country_name])
#         list_items += f'<li><a href="{country_path}">{country_name}</a></li>'
#
#     responde_data = f'<h1>Kraje</h1><ul>{list_items}</ul>'
#     return HttpResponse(responde_data)

def country_list(request, count):
    return render(request, 'podstawy/country_list.html', {
        'country_list': all_countries[:count]
    })

    responde_data = f'<h1>Kraje</h1><ul>{list_items}</ul>'
    return HttpResponse(responde_data)


def first_template(request):
    return render(request, 'podstawy/first_template.html')
