from django.shortcuts import render, render_to_response,Http404, get_object_or_404, loader
import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect

def index(request):
    smart = ['Specific', 'Measurable', 'Achievable', 'Relevant', 'Time bound']
    #return render_to_response("index.html", {'smart':smart})
    return render(request, "index.html", {'smart':smart})

def login(request):
    if request.method == 'POST':
        print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404
