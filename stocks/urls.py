from django.urls import path
from . views import home, update_stock, delete_stock

urlpatterns = [
    path('', home, name='home'),

    path('update_stock/<int:stock_id>/', update_stock, name='update_stock'),
    path('delete_stock/<int:stock_id>/', delete_stock, name='delete_stock')
]