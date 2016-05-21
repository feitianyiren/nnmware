# -*- coding: utf-8 -*-
# nnmware(c)2012-2016
# Admin config

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreAppConfig(AppConfig):
    name = "core"
    verbose_name = _("Core engine")
