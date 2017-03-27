from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import People, Article, Comment
from django.template import Context, Template
from firstapp.form import CommentForm


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
    contect = {}
    comment_list = Comment.objects.all()
    contect['comment_list'] = comment_list
    contect['form'] = form
    return render(request, 'detail.html', contect)
