from django.shortcuts import render
from firstapp.models import Article
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    article_list = Article.objects.all()
    page_robot = Paginator(article_list, 9)
    article_list = page_robot.page(request.GET.get('page'))
    context = {}
    context["article_list"] = article_list

    return render(request, 'index.html', context)
