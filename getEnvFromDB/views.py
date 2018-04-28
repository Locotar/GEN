from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from main.SQlitDB import connect_db


def getEnvFromDB(request):
    username = request.session.get('username')
    if username:
        conn = connect_db()
        value = conn.selectfromtable('env', 'id,name,ip,jointime,lock,status')
        if value:
            return render(request, 'env_table.html', {'dict': value})
        else:
            # show error msg
            return HttpResponseRedirect('/login/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')

