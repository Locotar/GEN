from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect

def getEnvFromDB(request):
    username = request.session.get('username')
    if username:
        return render( request ,'env_table.html' , {'username': 'c','active': 'env'})
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')
