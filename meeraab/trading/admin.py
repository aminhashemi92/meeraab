from django.contrib import admin
from .models import *
# Register your models here.
class TradeAdmin(admin.ModelAdmin):
    list_display = ('creator','well','type','amount','price','status','jpublish','jexpire',)
    list_filter = (['type','status'])
    search_fields = ('creator', 'well')
    prepopulated_fields = {'slug':('well',)}

admin.site.register(Trade,TradeAdmin)
