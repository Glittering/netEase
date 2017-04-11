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


# def detail_old(request,page_num):
#     if request.method == 'GET':
#         form = CommentForm
#     elif request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             comment = form.cleaned_data['comment']
#             a = Article.objects.get(id=page_num)
#             c = Comment(name=name, comment=comment)
#             c.save()
#             return redirect(to='detail', page_num=page_num, belong_to=a)
#     context = {}
#     a = Article.objects.get(id=page_num)
#     best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
#     if best_comment:
#         context['best_comment'] = best_comment[0]
#     # comment_list = Comment.objects.all();
#     article = Article.objects.get(id=page_num)
#     context['article'] = article
#     # context['comment_list'] = comment_list
#     context['form'] = form
#     return render(request, 'detail.html', context)
#

def detail(request, page_num, error_form=None):
    context = {}
    form = CommentForm
    a = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
    if best_comment:
        context['best_comment'] = best_comment[0]
    # comment_list = Comment.objects.all();
    article = Article.objects.get(id=page_num)
    context['article'] = article
    # context['comment_list'] = comment_list
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'detail.html', context)


def detail_comment(request, page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        a = Article.objects.get(id=page_num)
        c = Comment(name=name, comment=comment, belong_to=a)
        c.save()
    else:
        return detail(request, page_num, error_form=form)
    return redirect(to='detail', page_num=page_num)
