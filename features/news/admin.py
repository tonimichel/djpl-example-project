from django.contrib import admin
from .models import NewsEntry




class NewsAdmin(admin.ModelAdmin):
    list_display = ['date', 'headline', 'published']
    
    

admin.site.register(NewsEntry, NewsAdmin)


