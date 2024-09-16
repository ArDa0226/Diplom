from django.contrib import admin
from django.template.defaultfilters import title

# Register your models here.
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'sex', 'time_create', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'surname')
    list_filter = ('time_create', 'time_update')
    prepopulated_fields = {'slug': ('name', 'surname')}

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)

