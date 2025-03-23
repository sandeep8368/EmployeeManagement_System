from django.contrib import admin
from empapp.models import empModel
# Register your models here.

class empModelAdmin(admin.ModelAdmin):
    list_display = ['name','phome','email','addr']
    
    
admin.site.register(empModel, empModelAdmin)