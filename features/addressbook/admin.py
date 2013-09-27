from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'employer', 'created']
    
    

admin.site.register(Contact, ContactAdmin)


