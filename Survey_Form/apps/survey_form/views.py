# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request, 'survey_form/index.html')

# Create your views here.
