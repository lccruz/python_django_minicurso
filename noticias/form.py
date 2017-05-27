# -*- coding:utf-8 -*-

from django import forms


class PesquisaForm(forms.Form):
    title = forms.CharField(label='Your name', max_length=100)
