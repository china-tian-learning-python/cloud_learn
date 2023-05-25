from django.contrib import admin
from .models import Department,UserInfo
# Register your models here.
# admin.site.register()


@admin.register(Department)
class DepartAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title']

@admin.register(UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','password','age','account','create_time','depart','six']
    fields = ['name','password','age','account','create_time','depart','six']