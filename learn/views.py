from django.shortcuts import render

# Create your views here.
# encoding : utf-8
from django.http import HttpResponse
 
def index(request):
    # return HttpResponse('hello world !')
    return render(request , 'home.html')
