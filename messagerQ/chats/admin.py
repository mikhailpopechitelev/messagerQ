from django.contrib import admin
from .models import * 

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','dateregistration')
    list_display_links = ('id','name')
    
    
admin.site.register(User,UserAdmin)