from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def captain(request):
    return HttpResponse('<h1>Ruthuraj is a captain of CSK</h1>')

def viceCaptain(request):
    return HttpResponse('<h1>Jadeja is a vicecaptain of CSK</h1>')
