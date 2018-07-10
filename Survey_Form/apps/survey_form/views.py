# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' not in request.session: 
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request, 'survey_form/index.html')

def postinfo(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['locations'] = request.POST['locations']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')
    
    # if 'count' not in request.session:
    #     request.session['count'] = 1
    # else:
    #     request.session['count'] += 1
    # print request.session['count']
    # request.session['count'] = request.POST['count']
    # request.session['name'] = request.POST['name']
    # request.session['location'] = request.POST['location']
    # request.session['language'] = request.POST['language']
    # request.session['comment'] = request.POST['comment']
    # print request.session
    # return redirect('/result')

def result(request):
    
    
    return render(request, 'survey_form/result.html')
    # context = {
    #     'count' : request.session['count'],
    #     'name' : request.session['name'],
    #     'location' : request.session['location'],
    #     'language' : request.session['language'],
    #     'comment' : request.session['comment']
    # }
    # print context
    # return render(request, 'survey_form/result.html', context)
