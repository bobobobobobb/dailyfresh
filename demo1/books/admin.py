from django.contrib import admin
from .models import HeroInfo, BookInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bread', 'bcomment']


admin.site.register(BookInfo, BookInfoAdmin)
