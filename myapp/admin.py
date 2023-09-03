from django.contrib import admin
from .models import Stockdata

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class StockdataResource(resources.ModelResource):
    class Meta:
        model=Stockdata

class Stockadmin(ImportExportModelAdmin):
    resources_class = StockdataResource
    list_display= ('date', 'trade_code','high','low','open','close')

admin.site.register(Stockdata,Stockadmin)
