from django.shortcuts import render,HttpResponse

def hi(request):
    return HttpResponse("hello")