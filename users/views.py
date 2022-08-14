from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))


def login(request):
    return render(request, 'users/login.html')
