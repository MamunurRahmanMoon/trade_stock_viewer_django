from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Stock

import pandas as pd

def home(request):
    # Retrieve all data from database
    stocks = Stock.objects.all()

    queryset = Stock.objects.values('date', 'close')
    df = pd.DataFrame.from_records(queryset)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)

    data = {
        'labels': df['date'].dt.strftime('%Y-%m-%d').tolist(),
        'close_prices': df['close'].tolist(),
    }

    return render(request, 'home.html', {'stocks': stocks, 'data': data})


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
    


# def getChart(request):
#     queryset = Stock.objects.values('date', 'close')
#     df = pd.DataFrame.from_records(queryset)
#     df['date'] = pd.to_datetime(df['date'])
#     df.sort_values('date', inplace=True)

#     data = {
#         'labels': df['date'].dt.strftime('%Y-%m-%d').tolist(),
#         'close_prices': df['close'].tolist(),
#     }

#     chart_html = render(request, 'chart.html', {'data': data})
#     return HttpResponse(chart_html)