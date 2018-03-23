# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, 'primeNumbers/index.html', { 'primes': "" })

def prime(request):
    if request.method == 'POST':
        error = Prime.objects.isValid(request.POST['max'])
        if len(error) > 0:
            print('error')
            messages.error(request, error['error'][0])
            return redirect('/')
        else:
            primes = "2"
            num = int(request.POST['max']) + 1
            # run the for loop
            primes = Prime.objects.getPrimes(num)
            return render(request, 'primeNumbers/index.html', { 'primes': primes })
    else:
        return redirect('/')