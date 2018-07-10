# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey_form/index.html')

def postinfo(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    print request.session['count']
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    context = {
        'count' : request.session['count'],
        'name' : request.session['name'],
        'location' : request.session['location'],
        'comment' : request.session['comment']
    }
    print context
    return render(request, 'result.html', context)
