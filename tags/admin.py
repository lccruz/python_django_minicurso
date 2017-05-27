from django.contrib import admin
from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Tag, TagAdmin)
