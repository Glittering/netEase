from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    web = render(request, 'list.html', context)
    return web
