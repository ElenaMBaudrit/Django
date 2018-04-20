# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    return render (request,'Amabon/index.html')

def purchase(request):
    if request.POST['product_name']=='dojotshirt':
        request.session['item_price'] = 19.99 * int(request.POST['amount_of_items'])

    if request.POST['product_name']=='dojotsweater':
        request.session['item_price'] = 29.99 * int(request.POST['amount_of_items'])

    if request.POST['product_name']=='dojocup':
        request.session['item_price'] = 4.99 * int(request.POST['amount_of_items'])

    if request.POST['product_name']=='algorithmbook':
        request.session['item_price'] = 49.99 * int(request.POST['amount_of_items'])

    if 'total_amount_of_items' not in request.session:
        request.session['total_amount_of_items'] = int(request.POST['amount_of_items'])
    else:
        request.session['total_amount_of_items'] =int(request.session['total_amount_of_items'])+int(request.POST['amount_of_items'])

    if 'total_price' not in request.session:
        request.session['total_price'] = request.session['item_price']
    else:
        request.session['total_price'] += request.session['item_price']
        
    return redirect ('/checkout')

def checkout(request):
    return render (request,'Amabon/checkout.html')

def clear(request):
    request.session.clear()
    # also, delete the color and font size information
    return redirect ('/')
