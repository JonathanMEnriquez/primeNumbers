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

class Prime(models.Model):
    objects = PrimeManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)