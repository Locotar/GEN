from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
# from login.views import login
from main.SQlitDB import connect_db
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def reportServer(request):
    username = request.session.get('username')
    if username:
        conn = connect_db()
        val = conn.selectfromtable('reportList')
        value = val.fetchall()
        # for
        paginator = Paginator(value, 15)
        page = request.GET.get('page')
        try:
            customer = paginator.page(page)
        except PageNotAnInteger:
            customer = paginator.page(1)
        except EmptyPage:
            customer = paginator.page(paginator.num_pages)
        return render(request, 'reportServer.html', {'username': username, 'active': 'reportServer',
                                                     'reList': customer, 'pg': paginator,
                                                     })
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')

