import json
from django.db import models


# Create your models here.

def load_countries():
    with open('Podstawy/country_info.json', encoding='UTF-8') as countries_file:
        return json.load(countries_file)


def find_by_name(name):
    for country in all_countries:
        if country['country'].casefold() == name.casefold():  # casefold() nie ma znaczenia wielkość znaków
            return country
    return None

all_countries = load_countries()
