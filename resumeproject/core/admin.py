from django.contrib import admin
from . models import contactmodel 
class contactadmin(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']
admin.site.register(contactmodel,contactadmin)

# Register your models here.
