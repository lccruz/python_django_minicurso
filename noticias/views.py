# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView
from noticias.models import Noticia
from tags.models import Tag


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.all()[:15]
        context['tags'] = Tag.objects.all()
        return context
