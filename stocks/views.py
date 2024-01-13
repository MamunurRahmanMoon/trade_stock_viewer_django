from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import json

def home(request):
    # Load JSON data
    with open('stocks\stocks.json') as json_file:
        stocks = json.load(json_file)

    return render(request, 'home.html', {'stocks': stocks})