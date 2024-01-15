from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Stock
import json

def home(request):
    # Retrieve all data from database
    stocks = Stock.objects.all()

    return render(request, 'home.html', {'stocks': stocks})


@csrf_exempt
def update_stock(request, stock_id):
    if request.method == 'POST':
        stock = Stock.objects.get(id=stock_id)
        stock.high = request.POST.get('high')
        stock.low = request.POST.get('low')
        stock.open = request.POST.get('open')
        stock.close = request.POST.get('close')
        stock.volume = request.POST.get('volume')
        stock.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

@csrf_exempt
def delete_stock(request, stock_id):
    if request.method == 'POST':
        stock = Stock.objects.get(id=stock_id)
        stock.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})