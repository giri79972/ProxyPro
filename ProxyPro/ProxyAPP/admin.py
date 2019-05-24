from django.contrib import admin

# Register your models here.
from .models import Emp,EmpProxy
class AdminEmp(admin.ModelAdmin):
    list_display = ['eno','ename','sal']
class AdminProxy(admin.ModelAdmin):
    list_display=['eno','ename','sal']
admin.site.register(EmpProxy,AdminProxy)
admin.site.register(Emp,AdminEmp)
