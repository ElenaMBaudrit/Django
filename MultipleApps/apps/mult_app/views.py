# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# the index function is called when root is visited
def index(request):
    response = "Hello, I am your Multiple Apps project!"
    return HttpResponse(response)
