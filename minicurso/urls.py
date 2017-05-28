"""minicurso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from noticias.views import HomePageView
from noticias.views import pesquisa
from tags.views import TagNoticiasListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^pesquisa/$', pesquisa, name='pesquisa'),
    url(r'^tag/([\w-]+)/$', TagNoticiasListView.as_view(), name='tag_noticias_list_view'),
]

if settings.DEBUG:
    urlpatterns += static('static', document_root=settings.STATIC_ROOT)
