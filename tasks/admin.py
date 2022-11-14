from django.contrib import admin
from django.contrib.auth.models import User
from tasks.models import task,time
from .models import *
# Register your models here.

class taskAdmin(admin.ModelAdmin):
    list_display = ('desc','complete','created')
    list_filter = ('created','complete')




admin.site.register(task,taskAdmin)
admin.site.register(time)
admin.site.site_header = 'ADMIN PAGE'
