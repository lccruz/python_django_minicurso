# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView
from noticias.models import Noticia


class HomePageView(TemplateView):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.all()[:15]
        return context
