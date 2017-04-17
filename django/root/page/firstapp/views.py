from django.shortcuts import render, Http404
from firstapp.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request, cate=None):
    article_list = Article.objects.all()
    page_robot = Paginator(article_list, 9)
    # article_list = page_robot.page(request.GET.get('page'))
    page_num = request.GET.get('page')
    context = {}
    try:
        vids_list = page_robot.page(page_num)
    except EmptyPage:
        vids_list = page_robot.page(page_robot.num_pages)
        # raise Http404('EmptyPage')
    except PageNotAnInteger:
        vids_list = page_robot.page(1)
    # context["article_list"] = article_list
    context["article_list"] = vids_list
    return render(request, 'index.html', context)
