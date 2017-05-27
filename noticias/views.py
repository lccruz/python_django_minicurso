# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from noticias.models import Noticia
from tags.models import Tag


class HomePageView(TemplateView):
    """
        TemplateView = https://docs.djangoproject.com/en/1.11/topics/class-based-views/#subclassing-generic-views
        Paginator = https://docs.djangoproject.com/en/1.11/topics/pagination/
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        noticias = Noticia.objects.all()
        paginator = Paginator(noticias, 10)
        page = self.request.GET.get('page')
        try:
            noticias = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            noticias = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999),deliver last page of results.
            noticias = paginator.page(paginator.num_pages)
        context['noticias'] = noticias
        context['tags'] = Tag.objects.all()
        return context
