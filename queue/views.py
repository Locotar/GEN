from django.shortcuts import render , render_to_response

# Create your views here.
from django.http import HttpResponse

def queue(request):
    return render(request ,'queue.html')
