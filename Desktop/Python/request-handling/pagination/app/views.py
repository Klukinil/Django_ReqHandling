from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from csv import DictReader
from urllib.parse import urlencode

with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as f:
    bus_stops = list(DictReader(f))


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stops, 10)
    page = paginator.get_page(current_page)
    data = page.object_list

    if page.has_next() == True:
        next_page_url = '?'.join((reverse('bus_stations'), urlencode({'page': page.next_page_number()})))
    else:
        next_page_url = None
    if page.has_previous():
        prev_page_url = '?'.join((reverse('bus_stations'), urlencode({'page': page.previous_page_number()})))
    else:
        prev_page_url = None

    return render(request, 'index.html', context={
        'bus_stations': data,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

