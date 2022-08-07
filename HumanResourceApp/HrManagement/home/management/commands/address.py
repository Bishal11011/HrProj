
from django.core.management.base import BaseCommand
from ...models import Provinces



class Command(BaseCommand):
    countries=[
    {
        "name": "Alberta",
        "abbreviation": "AB"
    },
    {
        "name": "British Columbia",
        "abbreviation": "BC"
    },
    {
        "name": "Manitoba",
        "abbreviation": "MB"
    },
    {
        "name": "New Brunswick",
        "abbreviation": "NB"
    },
    {
        "name": "Newfoundland and Labrador",
        "abbreviation": "NL"
    },
    {
        "name": "Northwest Territories",
        "abbreviation": "NT"
    },
    {
        "name": "Nova Scotia",
        "abbreviation": "NS"
    },
    {
        "name": "Nunavut",
        "abbreviation": "NU"
    },
    {
        "name": "Ontario",
        "abbreviation": "ON"
    },
    {
        "name": "Prince Edward Island",
        "abbreviation": "PE"
    },
    {
        "name": "Quebec",
        "abbreviation": "QC"
    },
    {
        "name": "Saskatchewan",
        "abbreviation": "SK"
    },
    {
        "name": "Yukon Territory",
        "abbreviation": "YT"
    }
]
    for i in countries:
        print(i['name'])
        prov=Provinces.objects.create(name=i['name'],code=i['abbreviation'])
        prov.save()

