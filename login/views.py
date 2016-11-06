#encoding : utf-8
from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.template import RequestContext
from login.models import User
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='user:',max_length=16)
    password = forms.CharField(label='pass:',widget=forms.PasswordInput())

def login(req ):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                # write to session
                req.session['username'] = username
                return HttpResponseRedirect('/env/')
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()

    regist =req.GET.get('regist')
    if regist:
        # return render_to_response('login.html', context_instance=RequestContext(req))
        return render_to_response('login.html',{'uf':uf , 'regist':'success'} , context_instance=RequestContext(req))
    else:
        return render_to_response('login.html',{'uf':uf} , context_instance=RequestContext(req))

def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # get values
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # wheter username exist!
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                return HttpResponse('Fail , username exit!')
            else:
                # add to db
                User.objects.create(username= username,password=password)
                # return HttpResponse('success!')
                # time.sleep(3)
                # return HttpResponseRedirect('/login/' ,{'uf':uf , 'regist':'success'})
                return HttpResponseRedirect('/login/?regist=success' )
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(request))

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})


def logout(req):
    response = HttpResponse('logout success!!')
    # clean username
    del req.session['username']

    return response
