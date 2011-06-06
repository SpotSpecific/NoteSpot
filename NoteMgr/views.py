# encoding: utf-8
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.models import Site, RequestSite
from django.views.decorators.cache import never_cache
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse

@login_required
def showall(request):
    print "notes.showall"
