from django.shortcuts import render, redirect
from django.http import HttpResponse

def django2(request):
    menu = [{'title': 'HOMIE PAGGEEE'}, {'title': 'helloworldiee'}, {'title': 'NAAAAAH man?'}]
    return HttpResponse("<h1>Home page</h1>")


def news(request):
    return HttpResponse(request, "morry/morry.html", {'title': "HOMIE page"})
