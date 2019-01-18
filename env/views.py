from django.shortcuts import render , render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse , HttpResponseRedirect, JsonResponse
from main.SQlitDB import connect_db
import time
import simplejson


def __unicode__(self):
   return unicode(self.some_field) or u''


def env(request):
    username = request.session.get('username')
    if username:
        conn = connect_db()
        value = conn.selectfromtable('env', 'id,name,ip,jointime,lock,status')
        if value:
            return render(request, 'env.html', {'username': username, 'active': 'env', 'dict': value})
        else:
            # show error msg
            return HttpResponseRedirect('/login/')
    else:
        # return login(request)
        return HttpResponseRedirect('/login/')


def AddEnv(request):
    if request.method == 'POST':
        envname = request.POST.get('envname')
        envip = request.POST.get('ip')
        envuser = request.POST.get('username')
        envpass = request.POST.get('pass')
        # if envmodule not N will use module to init it
        envmodule = request.POST.get('envmodule')

        conn = connect_db()
        # jointime = time.strftime("%Y-%m-%d-%H:%M:%S").decode('GBK').encode('utf-8') + "'"
        value = "'" + envname + "','" + envip + "','" + envuser + "','" + envpass + "','" \
               + time.strftime("%Y-%m-%d %H:%M:%S") + "','None','None','None','None','None','None','None'"
        
        # raise Exception(value)
        addflag = conn.Addtotable('env', value)
        if addflag:
            # add success
            return HttpResponseRedirect('/env/')
        else:
            # add fail
            return HttpResponseRedirect('/login/')


def CheckEnv(request):
    envip = request.GET.get('envip')
    conn = connect_db()
    value = conn.selectfromtable('env', 'ip')
    if value:
        for env in value:
            if envip in env:
                result = {'result': 'Exist'}
                return JsonResponse(result)
        result = {'result': 'notExist'}
        return JsonResponse(result)
    else:
        result = {'result': 'notExist'}
        return JsonResponse(result)


def ShowEnvHTMLTemplate(request):
    if request.is_ajax():
        do = request.POST.get('do')
        if do == 'add':
            module = {'Default'}
            info_dict = {'title': 'Add Env', 'fun': 'subAddEnv()', 'action': "action=/env/AddEnv/"
                , 'module': module}
        elif do == 'mod':
            userid = request.POST.get('userId')
            userName = request.POST.get('userName')
            info_dict = {'title': 'Modify User','username': userName, 'username_disable': 'disabled=true'
                , 'fun': "subModUser('" + str(userid) +"','" + userName + "' )"}
        html = render_to_string('envinfotmp.html', {'info_dict': info_dict} )
        return HttpResponse(html)


def DelEnv(request):
    username = request.session.get('username')
    if username:
        envid = request.GET.get('envid')
        try:
            conn = connect_db()
            value = conn.selectfromtable('env', envid)
            if value:
                conn.deletefromtable('env', envid)
                result = simplejson.dumps('success')
                return HttpResponse(result, mimetype='application/javascript')
        # raise Exception(value.fetchall())
        except:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')
