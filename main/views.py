from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main(request):
    return render(request , 'success.html')
