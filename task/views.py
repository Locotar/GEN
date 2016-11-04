from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
# from login.views import login

def task(request):
    username = request.session.get('username')
    if username:
        return render(request ,'task.html', {'username':username,'active': 'task'})
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')

