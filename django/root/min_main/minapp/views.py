from django.shortcuts import render
from minapp.models import Article

# Create your views here.


def index(request):
    querySet = request.GET.get('tag')
    if querySet:
        article_list = Article.objects.filter(tag=querySet)
    else:
        article_list = Article.objects.all()
    context = {}
    context['article_list'] = article_list
    web = render(request, 'list.html', context)
    return web
