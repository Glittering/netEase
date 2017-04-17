from django.shortcuts import render, redirect, HttpResponse
from firstapp.models import Article, Comment, Ticket
from firstapp.forms import CommentForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.

def index(request):
    article_list = Article.objects.all()

    page_robot = Paginator(article_list, 5)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context = {}
    context["article_list"] = article_list

    return render(request, 'index.html', context)

def detail(request, id):
    context = {}
    article = Article.objects.get(id=id)
    like_counts = Ticket.objects.filter(choice='like', article_id=id).count()
    try:
        voter_id = request.user.profile.id
        user_ticket_for_video = Ticket.objects.get(voter_id=voter_id, article_id=id)
        context['user_ticket'] = user_ticket_for_video
    except:
        pass
    if request.method == "GET":
        form = CommentForm
    context['like_counts'] = like_counts
    context["article"] = article
    context['form'] = form

    return render(request, 'detail.html', context)

def detail_vote(request, id):
    voter_id = request.user.profile.id

    try:
        user_ticket_for_video = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_video.choice = request.POST['vote']
        user_ticket_for_video.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, video_id=id, choice=request.POST('vote'))
        new_ticket.save(force_insert=False, force_update=False, using=None, update_fields=None)
    return redirect(to='detail',id=id)

def comment(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            comment = form.cleaned_data["comment"]
            article = Article.objects.get(id=id)
            c = Comment(name=name, comment=comment, belong_to=article)
            c.save()
            return redirect(to="detail", id=id)
    return redirect(to="detail", id=id)

def login_def(request):
    context = {}
    if request.method == 'GET':
        # form = LoginForm
        form = AuthenticationForm
    else:
        # form = LoginForm(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # res = authenticate(username=username, password=password)
            login(request, form.get_user(), backend=None)
            return redirect(to='index')
            # if res:
            #     login(request, res)
            #     return redirect(to='index')
            # else:
            #     return HttpResponse('<h1>ERROR!<h1>')
    context['form'] = form
    return render(request, 'login.html', context=context, content_type=None, status=None, using=None)

def register_def(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    elif request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form']=form
    return render(request, 'register.html', context=context, content_type=None, status=None, using=None)
