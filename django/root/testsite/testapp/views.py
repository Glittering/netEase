from django.shortcuts import render, HttpResponse, redirect
from testapp.models import Person, Article, Comment
from django.template import Context, Template
from testapp.form import CommentForm
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
    querySet = request.GET.get('tag')
    if querySet:
        article_List = Article.objects.filter(tag=querySet)
    else:
        article_List = Article.objects.all()
    context = {'article_List': article_List}
    web = render(request, 'first_web_2.html', context)
    return web


def bing(request):
    bing = render(request, 'bing_ser.html')
    return bing


def detail(request):
    if request.method == 'GET':
        form = CommentForm
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            c = Comment(name=name, comment=comment)
            c.save()
            return redirect(to='detail')
    context = {}
    comment_list = Comment.objects.all();
    context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'detail.html', context)
