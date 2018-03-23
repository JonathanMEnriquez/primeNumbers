# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PrimeManager(models.Manager):
    def isValid(self, postData):
        response = {}
        try:
            if int(postData) < 2:
                response['error'] = []
                response['error'].append("Number must be greater than 1")
        except:
            response['error'] = []
            response['error'].append("Please enter valid data")
        return response
    
    def getPrimes(self, max):
        primes = "2"
        for i in range(3, max, 2):
            isPrime = True
            for j in range(3, (i / 2), 2):
                if i % j == 0 & i != j:
                    isPrime = False
                    break
            if isPrime == True:
                primes += ", {}".format(i)
        return primes

class Prime(models.Model):
    objects = PrimeManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)