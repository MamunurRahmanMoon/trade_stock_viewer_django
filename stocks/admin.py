from django.contrib import admin
from .models import Stock
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class StockAdmin(ImportExportModelAdmin):
    list_display = ['id', 'date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']

admin.site.register(Stock, StockAdmin)