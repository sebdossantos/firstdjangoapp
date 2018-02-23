from django.shortcuts import render


def blank(request):
    return render(request, 'mytheme/blank.html')


def cards(request):
    return render(request, 'mytheme/cards.html')


def charts(request):
    return render(request, 'mytheme/charts.html')


def forgot_password(request):
    return render(request, 'mytheme/forgot-password.html')


def index(request):
    return render(request, 'mytheme/index.html')


def login(request):
    return render(request, 'mytheme/login.html')


def navbar(request):
    return render(request, 'mytheme/navbar.html')


def register(request):
    return render(request, 'mytheme/register.html')


def tables(request):
    return render(request, 'mytheme/tables.html')
