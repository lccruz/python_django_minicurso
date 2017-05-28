# -*- coding: utf-8 -*-

import time
from django.test import TestCase
from datetime import datetime
from utils.utils import converte_data
from utils.utils import verifica_thumbnail
from utils.utils import get_reddit_noticias
from utils.utils import get_local_noticias
from utils.utils import salva_noticias
from noticias.models import Noticia
from tags.models import Tag


class ModelsTestCase(TestCase):
    def setUp(self):
        get_reddit_noticias()
        salva_noticias()

    def testConverteData(self):
        """
            testa se o converte_data ira retornar um datetime
        """
        data = datetime(1970, 1, 1)
        data_timestamp = data.timestamp()
        self.assertFalse(converte_data(''))
        self.assertEqual(converte_data(data_timestamp), data)

    def testThumbnail(self):
        """
            testa se o thumbnail é uma url
        """
        thumbnail = "http://www.baitainf.com.br"
        self.assertEqual(verifica_thumbnail(thumbnail), thumbnail)
        self.assertFalse(verifica_thumbnail("BaitaInf"))

    def _testRedditNoticias(self):
        """
            testa conexão com REDDIT
            servidor do REDDIT responde com 429 (Too Many Requests)
            se executado muitas vezes o get_reddit_noticias
        """
        time.sleep(5)
        noticias = get_reddit_noticias()
        self.assertTrue(noticias)
        noticias = get_reddit_noticias()
        self.assertFalse(noticias)

    def testLocalNoticias(self):
        """
            teste se conseguiu ler o arquivo utils/dados.json
        """
        noticias = get_local_noticias()
        self.assertTrue(noticias)

    def testNoticiasCriadas(self):
        """
            testa se as noticias foram lidas do site do Reddit ou do
            arquivo utils/dados.json e inseridas no banco de dados
        """
        noticias = Noticia.objects.all()
        # testa se tem 25 noticias no banco de dados
        self.assertEqual(noticias.count(), 25)
        noticia = Noticia.objects.get(id_reddit="6deuhp")
        # testa se a url é igual a url da noticia id 6deuhp do utils/dados.json
        self.assertEqual(noticia.url, "https://i.redd.it/8lsahhntxrzy.jpg")
        tag = Tag.objects.get(title="pics")
        # testa se efetuou a ligacao noticia com a tag
        self.assertEqual(noticia.tags.all()[0].title, tag.title)

    def testHome(self):
        """
            testa a se view home retorna 10 noticias e 25 tags
        """
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        noticias = response.context['noticias'].object_list
        self.assertEqual(len(noticias), 10)
        tags = response.context['tags']
        self.assertEqual(tags.count(), 25)
        self.assertTrue(tags.filter(title='pics'))

        # testa se trocou de pagina
        response = self.client.get('/?page=2')
        self.failUnlessEqual(response.status_code, 200)
        noticias = response.context['noticias'].object_list
        self.assertEqual(len(noticias), 10)

    def testPesquisa(self):
        """
            testa view pesquisa
        """
        response = self.client.post("/pesquisa/", {'title':'day'})
        self.assertEqual(response.context['termo_pesquisado'], 'day')
        noticias = response.context['noticias']
        self.assertEqual(noticias.count(), 2)
        for noticia in noticias:
            self.assertTrue('day' in noticia.title)
