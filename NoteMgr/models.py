# -*- coding: utf-8 -*-
from django.db import models
from django.template import Context, Template
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from uuid import uuid4

class Note(models.Model):
    name = models.CharField(max_length=120,help_text="Displayed name of this item")
    slug = models.CharField(max_length=32,help_text="Slug Field, used for short URLs", blank=True, null=True)
    body = models.TextField(help_text='Actual Notefield', blank=True, null=True)
# UUIF field, used for internal lookups
    uuid = models.CharField(max_length=64, editable=False, blank=True, default=uuid4, unique=True)
    
    owner = models.ForeignKey(User)
    created_date = models.DateTimeField('date created',auto_now_add=True)
    modified_date = models.DateTimeField('date modified',auto_now=True)

    def __unicode__(self):
        return self.name+" ("+slug+")"
