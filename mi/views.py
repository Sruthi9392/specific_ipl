from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def captain(request):
    return HttpResponse('<h1>HP is a captain of mi</h1>')