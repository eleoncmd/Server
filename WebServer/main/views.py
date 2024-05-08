from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def result(request):
    return render(request, 'main/result.html')


def info(request):
    return render(request, 'main/info.html')


def error(request):
    return render(request, 'main/error.html')
