from django.shortcuts import render , render_to_response
# from login.views import login
from django.http import HttpResponse , HttpResponseRedirect

def env(request ):
    username = request.session.get('username')
    if username:
        return render( request ,'env.html' , {'username': username,'active': 'env'})
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')
