from django.shortcuts import render , render_to_response
from django import forms
from django.http import HttpResponse , HttpResponseRedirect
from django.template import RequestContext
from login.models import User

def usermanage(request):
    return render(request ,'usermanage.html')

class UserForm(forms.Form):
    username = forms.CharField(label='user:',max_length=100)
    password = forms.CharField(label='pass:',widget=forms.PasswordInput())

def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # get values
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # add to db
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(request))
