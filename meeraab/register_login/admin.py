from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company','status','confirmed','role_to_str','pic_tag')
    ordering = ['user', 'company','status']
    list_filter = ('role','status','confirmed')
    search_fields = ('company','user',)

    def role_to_str(self, obj):
        return "، ".join([role.title for role in obj.role.all()])
    role_to_str.short_description = "نقش‌ها"

admin.site.register(Profile,ProfileAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('parent', 'title','status','position')
    ordering = ['parent', 'title', 'status']
    list_filter = ('title','parent', 'status')

admin.site.register(Role,RoleAdmin)
