from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from login.views import login

def queue(request):
    username = request.session.get('username')
    if username != None:
        return render(request ,'queue.html' , {'username' : username})
    else:
        return login(request)
