from django.shortcuts import render , render_to_response

# Create your views here.
from django.http import HttpResponse

def main(request):
    name=u'cahesi'
    return render(request ,'success.html' , {'name':name})
