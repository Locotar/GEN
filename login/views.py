#encoding : utf-8
from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.template import RequestContext
from login.models import User
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='user:',max_length=100)
    password = forms.CharField(label='pass:',widget=forms.PasswordInput())

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # get values
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # add to db
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                # write to session
                req.session['username'] = username
                # return render_to_response('env.html',{'username':username})
                return HttpResponseRedirect('/env/')
                # response.set_cookie('username',username,3600)
                # return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf} , context_instance=RequestContext(req))


def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})


def logout(req):
    response = HttpResponse('logout !!')
    # clean username
    response.delete_cookie('username')
    return response
