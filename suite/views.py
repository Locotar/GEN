from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from login.views import login

def suite(request):
    username = request.session.get('username')
    if username != None:
        return render(request ,'suite.html' , {'username': username})
    else:
        return login(request)
