# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = 'base.html'
