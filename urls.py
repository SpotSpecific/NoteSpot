# encoding: utf-8
# urls.py

import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^accounts/', include('UserMgr.urls')),

    (r'^notes/', include('NoteMgr.urls')),
    
#####################
# For Testing
#####################
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT, 'show_indexes':'True'}),
    (r'^E$', 'NoteMgr.views.showall', {'format':'JSON'}, 'api.notes.showall'),
    (r'^$', 'NoteMgr.views.showall', {}, 'notes.showall'),
)
