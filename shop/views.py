from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h1>HELLO</h1>")
