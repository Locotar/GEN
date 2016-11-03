from django.shortcuts import render , render_to_response
from login.views import login
from django.http import HttpResponse

def env(request):
    username = request.session.get('username')
    if username != None:
        return render( request ,'env.html' , {'username': username})
    else:
        # return render( request ,'login.html',{'uf': UserForm()})
        return login(request)
