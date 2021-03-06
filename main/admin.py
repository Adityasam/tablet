from django.contrib import admin
from .models import Database, Center
# Register your models here.

class DbAdmin(admin.ModelAdmin):
    list_display=['imei','brand','tab_id','current_center','received','allotted_to']
    list_editable=['brand','tab_id','current_center','received','allotted_to']

admin.site.register(Database, DbAdmin)

class CenterAdmin(admin.ModelAdmin):
    list_display=['center_id','name','allotted']

admin.site.register(Center, CenterAdmin)