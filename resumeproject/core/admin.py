from django.contrib import admin
from . models import contactmodel 
class contactadmin(admin.ModelAdmin):
    fields=['name','email','phone','message']
admin.site.register(contactmodel,contactadmin)

# Register your models here.
