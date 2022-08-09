from django.contrib import admin
from .models import *


# actions
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "انتشار خبرهای انتخاب شده"

def make_draf(modeladmin, request, queryset):
    queryset.update(status='d')
make_draf.short_description = "پیش نویس شدن خبرهای انتخاب شده"

def make_active(modeladmin, request, queryset):
    queryset.update(status=True)
make_active.short_description = "فعال شدن دسته‌بندی‌های انتخاب شده"

def make_diactive(modeladmin, request, queryset):
    queryset.update(status=False)
make_diactive.short_description = "غیرفعال شدن دسته‌بندی‌های انتخاب شده"



# Register your models here.
class WellAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'license', 'useType', 'status')
    list_filter = (['useType','status'])
    search_fields = ('owner', 'license')
    prepopulated_fields = {'slug':('name',)}
    actions = [make_active, make_diactive]

admin.site.register(Well,WellAdmin)


class WellPhysicalInfoAdmin(admin.ModelAdmin):
    list_display = ('well','area','depth','buyCap','sellCap','wellCap',)
    list_filter = (['well','area'])
    search_fields = ('well', 'area')

admin.site.register(WellPhysicalInfo,WellPhysicalInfoAdmin)



class ChahVandAdmin(admin.ModelAdmin):
    list_display = ('accountID','currentcharge','status',)
    list_filter = (['status',])
    search_fields = ('owner', 'accountID')
    actions = [make_active, make_diactive]

admin.site.register(ChahVand,ChahVandAdmin)


class AbVandAdmin(admin.ModelAdmin):
    list_display = ('accountID','currentcharge','status',)
    list_filter = (['status',])
    search_fields = ('owner', 'accountID')
    actions = [make_active, make_diactive]

admin.site.register(AbVand,AbVandAdmin)


class ChahAdmin(admin.ModelAdmin):
    list_display = ('accountID','currentcharge','status',)
    list_filter = (['status',])
    search_fields = ('owner', 'accountID')
    actions = [make_active, make_diactive]

admin.site.register(Chah,ChahAdmin)


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','idNumber','phoneNumber','well','status',)
    list_filter = (['status',])
    search_fields = ('beneficiary', 'well')
    actions = [make_active, make_diactive]

admin.site.register(Beneficiary,BeneficiaryAdmin)
