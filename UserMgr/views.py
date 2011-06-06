from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from helpers import safepost

def login(request):
    if request.POST:
        username = safepost(request,'u')
        password = safepost(request,'p')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                iprint('# Redirect to a success page.')
            else:
                print('# Return a "disabled account" error message')
        else:
            print('# Return an "invalid login" error message.')
    else:
        return render_to_response('login.html')
