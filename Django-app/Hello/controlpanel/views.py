from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Welcome to the World's Smartest Control Panel")

def files(request):
    return HttpResponse("Explore through all kinds of Entities")

def more(request):
    return HttpResponse("and more...")
