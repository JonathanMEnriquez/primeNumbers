# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, 'primeNumbers/index.html')

def prime(request):
    if request.method == 'POST':
        error = Prime.objects.isValid(request.POST)
        if len(error) > 0:
            for message in error['error']:
                messages.error(request, message)
            return redirect('/')
        else:
            num = int(request.POST['max'])
            print num
            
            # run the for loop
            for i in 1 ... num :
                print i
    else:
        return redirect('/')
    return    
