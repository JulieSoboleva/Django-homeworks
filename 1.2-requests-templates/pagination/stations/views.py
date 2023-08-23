import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    row_count = 20  # 1000
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        content = []
        for row in reader:
            content.append({'Name': row['Name'],
                            'Street': row['Street'],
                            'District': row['District']})
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(content, row_count)
    page = paginator.get_page(page_number)
    start_index = (page_number - 1) * row_count
    context = {
        'bus_stations': content[start_index:start_index + row_count],
        'page': page,
    }
    return render(request, 'stations/index.html', context)
