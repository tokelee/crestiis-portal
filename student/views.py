from django.shortcuts import render, HttpResponse

def index_page(request):
    return HttpResponse('<h1>Student<h1/>')