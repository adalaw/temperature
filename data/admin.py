from django.contrib import admin
from .models import *

class CsvAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'timestamp', 'activated')

admin.site.register(Csv, CsvAdmin)
admin.site.register(Temperature)

