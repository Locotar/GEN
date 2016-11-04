from django.shortcuts import render , render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# from login.views import login

def suite(request):
    username = request.session.get('username')
    if username:
        return render(request ,'suite.html' , {'username': username , 'active': 'suite'})
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')
