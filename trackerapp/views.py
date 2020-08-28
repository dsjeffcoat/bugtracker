from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from myusers.models import CustomUser

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_detail_view(request, user_id):
    pass


def ticket_detail_view(request, ticket_id):
    pass


def register_view(request):
    pass


def login_view(request):
    pass


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
