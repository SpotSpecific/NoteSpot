from django.conf import settings
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from NoteSpot.NoteMgr.models import *
from NoteSpot.common.widgets import *


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.fields['slug'].widget = SlugFieldWidget()
    class Meta:
        model = Note

