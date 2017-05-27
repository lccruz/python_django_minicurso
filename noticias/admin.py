from django.contrib import admin
from noticias.models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'selftext', 'tags__title')

admin.site.register(Noticia, NoticiaAdmin)
