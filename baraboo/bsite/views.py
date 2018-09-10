'''
from django.http import HttpResponse


def index(request):
    return HttpResponse('bsiteViews/Animation.html')

'''

from django.shortcuts import render_to_response

def index (request):
    return render_to_response('baraboo.html')