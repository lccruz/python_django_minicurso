# -*- coding:utf-8 -*-

from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from tags.models import Tag


class TagNoticiasListView(ListView):
    """
        ListView = https://docs.djangoproject.com/en/1.11/topics/class-based-views/generic-display/#dynamic-filtering
    """

    model = Tag
    template_name = 'tag_noticias_list_view.html'

    def get_context_data(self, **kwargs):
        context = super(TagNoticiasListView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, title=self.args[0])
        return self.tag.noticia_set.all()
