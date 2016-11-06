from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
# from django.template import Re/q/uestContext  HttpResponse ,, render_to_response
from login.models import User
import time
from main.SQlitDB import connect_db
# from login.views import login
import simplejson


def usermanage(request):
    username = request.session.get('username')
    if username:
        conn = connect_db()
        value = conn.selectfromtable('login_user' )
        if value:
            return render(request, 'usermanage.html', {'username': username,  'active': 'user', 'Userdict': value})
        else:
            # show error msg
            return HttpResponseRedirect('/login/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')

class UserForm( forms.Form ):
    username = forms.CharField(label='user:', max_length=100)
    password = forms.CharField(label='pass:', widget=forms.PasswordInput())



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
            return HttpResponseRedirect('/login/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')


def AddUser(request):
    username = request.session.get('username')
    if username:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            admin = request.POST.get('admin')
            # check whether already in db
            conn = connect_db()
            userexist = User.objects.filter(username__exact=username, password__exact=password)
            if userexist:
                return HttpResponseRedirect('/usermanage/')
            else:
                # add to db
                value = "'" + username + "','" + password + "','" \
                        + admin + "','" + str(time.strftime("%Y-%m-%d %H:%M:%S'"))
                addflag = conn.Addtotable('login_user', value)
                if addflag:
                    # add success
                    pass
                else:
                    # add fail
                    return HttpResponseRedirect('/login/')
            return HttpResponseRedirect('/usermanage/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')

def DelUser(request):
    username = request.session.get('username')
    if username:
        userid = request.GET.get('userid')
        # judge the userid whether exist
        try:
            conn = connect_db()
            value = conn.selectfromtable('login_user', userid)
            if value:
                # begin to delete from the login_user table
                conn.deletefromtable('login_user', userid)
                result = 1
                result = simplejson.dumps(result)
                return HttpResponse(result, mimetype='application/javascript')
        except:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')
