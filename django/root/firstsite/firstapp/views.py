from django.shortcuts import render, HttpResponse
from firstapp.models import People, Article
from django.template import Context, Template
# Create your views here.


def first_try(request):
    person = People(name='spock', job='officer')
    html_string = '''
        <html>
            <body>
            Hello,The {{person.job}} {{person.name}}
            </body>
        </html>
    '''
    t = Template(html_string)
    c = Context({'person': person})
    web_page = t.render(c)
    return HttpResponse(web_page)


def index(request):
    queryset = request.GET.get('tag')
    if queryset:
        article_List = Article.objects.filter(tag=queryset)
    else:
        article_List = Article.objects.all()
    context = {}
    context['article_List'] = article_List
    web_page_2 = render(request, 'first_web_2.html', context)
    return web_page_2
