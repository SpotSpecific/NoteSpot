from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'NoteMgr.views.showall', {}, 'notes.showall'),
    (r'^new/$', 'NoteMgr.views.add', {}, 'notes.add'),

)

