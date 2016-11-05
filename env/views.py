from django.shortcuts import render , render_to_response
# from login.views import login
from django.http import HttpResponse , HttpResponseRedirect
from main.SQlitDB import connect_db

def env(request ):
    username = request.session.get('username')
    if username:
        conn = connect_db()
        value = conn.selectfromtable('login_user' )
        if value:
            return render( request ,'env.html' , {'username': username,'active': 'env' , 'dict':value})
        else:
            # show error msg
            return HttpResponseRedirect('/login/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')
