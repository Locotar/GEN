from django.shortcuts import render , render_to_response
from django import forms
from django.http import HttpResponse , HttpResponseRedirect
from django.template import RequestContext
from login.models import User
import time
from main.SQlitDB import connect_db
# from login.views import login

def usermanage(request):
    username = request.session.get('username')
    if username :
        conn = connect_db()
        value = conn.selectfromtable('login_user' )
        if value:
            return render(request ,'usermanage.html' , {'username': username,'active': 'user' ,'Userdict': value})
        else:
            # show error msg
            return HttpResponseRedirect('/login/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')

class UserForm(forms.Form):
    username = forms.CharField(label='user:',max_length=100)
    password = forms.CharField(label='pass:',widget=forms.PasswordInput())



# button click
def ShowUser(request):
    username = request.session.get('username')
    if username:
        conn = connect_db()
        value = conn.selectfromtable('login_user' )
        if value:
            return render( request ,'User_table.html' , {'Userdict':value})
        else:
            # show error msg
            return Http404()
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')


def AddUser(request):
    username = request.session.get('username')
    if username:
        conn = connect_db()
        value = conn.selectfromtable('login_user' )
        if value:
            return render( request ,'User_table.html' , {'Userdict':value})
        else:
            # show error msg
            return HttpResponseRedirect('/login/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')