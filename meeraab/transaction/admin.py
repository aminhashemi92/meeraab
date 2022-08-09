from django.contrib import admin
from .models import *
# Register your models here.


class BucketAdmin(admin.ModelAdmin):
    list_display = ('name','source_well',)
    list_filter = (['source_well',])
    search_fields = ('name',)
admin.site.register(Bucket,BucketAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type','amount',)
    list_filter = (['type',])
    search_fields = ('type',)
admin.site.register(Transaction,TransactionAdmin)

class CreditAdmin(admin.ModelAdmin):
    list_display = ('bucket','credit','precredit')
    list_filter = (['bucket',])
    search_fields = ('bucket',)
admin.site.register(Credit,CreditAdmin)
