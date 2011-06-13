#!/usr/bin/env python
import os
os.system("python manage.py syncdb")
from django.core.management import setup_environ
import sys
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

setup_environ(settings)

from NoteSpot.UserMgr.models import *
from django.contrib.auth.models import User
from NoteSpot.NoteMgr.models import *

def get_help_email():
    help_email = raw_input("Email address for new (help) user for this install (can be same as admin account created above)?")

    if not help_email:
        return get_help_email()
    return help_email

def main():
    help_email = get_help_email()
    help_user = User.objects.filter(pk=1)[0]

    print "Creating setup for admin: "+help_email+"\n\n"

    # Check for help user
    help_test = User.objects.filter(username='help')
    if (len(help_test) > 0):
        sys.stderr.write("Error: User 'help' already exists....\n")
        help_user = help_test[0]
    	if help_user.email == help_email:
            sys.stderr.write("Fixed: ....but help 'email' matches, continueing to create helpfiles.\n")
        else:
            sys.stderr.write("Fatal: ....and help 'email' does not match that given above.\n     :\n     : If you really want to run this script either give the current help\n     : email address or delete the current help user...\n")
    else:
        print "Creating help user"
        help_user = User.objects.create_user(username='help', email=help_email, password='c3ntr4l')
        help_user.first_name = 'help'
        help_user.last_name = 'user'
        help_user.is_active = True
        help_user.save()

if __name__ == "__main__":
    main()
