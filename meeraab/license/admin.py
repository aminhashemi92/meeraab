from django.contrib import admin
from .models import *
# Register your models here.
class ChargeAndCreditAdmin(admin.ModelAdmin):
    list_display = ('creator','well','annual_charge','used_charge','remaining_charge','status',)
    list_filter = (['status',])
    search_fields = ('creator', 'well')

admin.site.register(ChargeAndCredit,ChargeAndCreditAdmin)


class TechnicalConditionAdmin(admin.ModelAdmin):
    list_display = ('creator','well','operation_license','calibrated','document','status',)
    list_filter = (['status',])
    search_fields = ('creator', 'well')

admin.site.register(TechnicalCondition,TechnicalConditionAdmin)


class ModifyNameAdmin(admin.ModelAdmin):
    list_display = ('creator','well','license','status',)
    list_filter = (['status',])
    search_fields = ('creator', 'well')

admin.site.register(ModifyName,ModifyNameAdmin)


class CommitmentAdmin(admin.ModelAdmin):
    list_display = ('creator','well','status',)
    list_filter = (['status',])
    search_fields = ('creator', 'well')

admin.site.register(Commitment,CommitmentAdmin)


class IssuanceAdmin(admin.ModelAdmin):
    list_display = ('creator','well','annual_charge','used_charge','remaining_charge','status',)
    list_filter = (['status',])
    search_fields = ('creator', 'well')

admin.site.register(Issuance,IssuanceAdmin)
