from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login as django_login

def login(request):
    if request.POST:
        username = request.POST.get('u', '')
        password = request.POST.get('p', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect(request.GET.get('next','/nonehere'))
            else:
                return render_to_response('login.html', { 'warning': "Account Disabled" })
        else:
            return render_to_response('login.html', { 'error': "Invalid Login" })
            print('# Return an "invalid login" error message.')
    else:
        return render_to_response('login.html')

def logout(request):
	return render_to_response('logout.html')
