from django.shortcuts import render, HttpResponse
from testapp.models import Person, Article
from django.template import Context, Template
# Create your views here.


def myWeb(request):
    person = Person(name='zhao', job='tee')
    html_do = '''
        <html>
            {{person.name}} is {{person.job}}
        </html>
    '''
    t = Template(html_do)
    c = Context({'person': person})
    web = t.render(c)
    return HttpResponse(web)


def index(request):
    article_List = Article.objects.all()
    context = {'article_List': article_List}
    web = render(request, 'first_web_2.html', context)
    return web
