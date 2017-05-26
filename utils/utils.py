# -*- coding:utf-8 -*-

import requests
import json
from datetime import datetime
from tags.models import Tag
from noticias.models import Noticia
from tags.models import Tag


URL = "https://www.reddit.com/r"


def converte_data(utc):
    """
        recebe uma data timestamp = 1495787160.0
        retorna data datetime.datetime(2017, 5, 26, 8, 26)
    """
    try:
        return datetime.fromtimestamp(utc)
    except:
        return False


def verifica_thumbnail(thumbnail):
    """
        verifica se o thumbnail é uma url
    """
    if 'http' in thumbnail:
        return thumbnail
    return ''


def get_reddit_noticias(tag="all"):
    """
        Conecta com o REDDIT
        REDDIT retorna no formato JSON
        por default são 25 noticias
        parametro tag=all, busca noticias gerais
    """
    url = "%s/%s/.json" % (URL, tag)
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    retorno = requests.get(url, headers=headers)
    if retorno.status_code == 200:
        return retorno.json()
    return False


def get_local_noticias():
    """
        Se o REDDIT bloquear temporatiamente o acesso
        utilizar essa função para seguir os estudos
    """
    arquivo = open("utils/dados.json", 'r').read()
    return json.loads(arquivo)


def salva_noticias():
    """
        Extrai informações do .json e salva no banco
    """
    noticias = get_reddit_noticias()
    if not noticias:
        noticias = get_local_noticias()

    # navega nos niveis do JSON
    # primeiro nivel do JSON data
    noticias = noticias.get('data', False)
    if not noticias:
        return False
    # nivel do JSON que contem as noticias
    noticias = noticias.get('children', False)
    if not noticias:
        return False

    # percorre a lista extraindo os dados da noticia
    for noticia in noticias:
        noticia = noticia.get('data')
        id_reddit = noticia.get('id')
        title = noticia.get('title')
        url = noticia.get('url')
        thumbnail = verifica_thumbnail(noticia.get('thumbnail'))
        created_utc = converte_data(noticia.get('created_utc'))
        selftext = noticia.get('selftext')
        subreddit = noticia.get('subreddit')
        # testa se noticia ja esta cadastrada
        noticia = Noticia.objects.filter(id_reddit=id_reddit)
        if noticia:
            continue

        if subreddit:
            tag = Tag.objects.get_or_create(title=subreddit)

        # salva noticia no bando de dados
        noticia = Noticia(
            id_reddit=id_reddit, title=title, url=url,
            thumbnail=thumbnail, created_utc=created_utc, selftext=selftext
        )
        noticia.save()

        # busca ou insere uma tag
        if subreddit:
            tag = Tag.objects.get_or_create(title=subreddit)
            # faz a relacao noticia com a tag
            noticia.tags.add(tag[0])
