# -*- coding: utf-8 -*-

from django.test import TestCase
from utils.utils import get_reddit_noticias
from utils.utils import salva_noticias


class ModelsTestCase(TestCase):
    def setUp(self):
        get_reddit_noticias()
        salva_noticias()

    def testTags(self):
        """
            testa a view tag_noticias_list_view
        """
        response = self.client.get('/tag/pics/')
        self.failUnlessEqual(response.status_code, 200)
        tag = response.context['tag']
        self.assertEqual(tag.title, 'pics')
        noticias = response.context['object_list']
        self.assertEqual(noticias.count(), 1)
        noticia = noticias[0]
        tags = noticia.tags.all()
        # testa se a tag tem ligacao com a noticia
        self.assertEqual(tags[0].title, 'pics')
