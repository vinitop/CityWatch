from django.shortcuts import render, HttpResponse

def index(request):
   
    return render(request,'index.html')
   # return HttpResponse("Welcome to the World's Smartest Control Panel")

def controlpanel(request):
    return HttpResponse("Comprehensive Surveillance and Analytics")


def files(request):
    return HttpResponse("Explore through all kinds of Entities")

def more(request):
    return HttpResponse("and more...")
