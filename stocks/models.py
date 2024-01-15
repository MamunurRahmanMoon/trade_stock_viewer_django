from django.db import models

# Create your models here.
class Stock(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=50)
    high = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    low = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    open = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    close = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)