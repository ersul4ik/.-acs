# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from applications.profiles.views import profile_edit, user_login, user_logout

urlpatterns = [
    url(r'logout/$', user_logout, name='user_logout'),
    url(r'login/$', user_login, name='user_login'),
    url(r'edit/(?P<user_id>\d+)/$', profile_edit, name='edit'),
    url(r'list/$', profile_edit, name='list'),
]
