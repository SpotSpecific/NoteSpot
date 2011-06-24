# encoding: utf-8
# UserMgr/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'login', 'UserMgr.views.login', {}, 'users.login'),
    (r'logout', 'UserMgr.views.logout', {}, 'users.logout'),
#    (r'create', 'UserMgr.views.create', {}, 'users.create'),
#    (r'confirm', 'UserMgr.views.confirm', {}, 'users.confirm'),
)
