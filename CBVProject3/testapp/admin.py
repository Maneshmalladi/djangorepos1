from django.contrib import admin

# Register your models here.
from .models import CompanyModel

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','company','ename','eid','eemail','ephn','esal']

admin.site.register(CompanyModel,CompanyAdmin)