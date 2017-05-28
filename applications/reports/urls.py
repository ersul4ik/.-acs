# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.reports import views

urlpatterns = [
    url(r'(\d+)/$', views.report_main, name='reports_page'),
]
