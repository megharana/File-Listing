from django.shortcuts import render
from django.http import HttpResponse


def testingUrl(request):
    return HttpResponse("Welcome")
