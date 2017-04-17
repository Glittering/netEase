from django.shortcuts import render, redirect
import sys

from firstapp.models import Article, Comment, Ticket, UserProfile
from firstapp.forms import CommentForm

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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
        voter_id = request.user.id
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

def index_login(request):
    if request.method == "GET":
        form = AuthenticationForm

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="index")

    context = {}
    context['form'] = form

    return render(request, 'login.html', context)

def index_register(request):
    if request.method == "GET":
        form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')

    context = {}
    context['form'] = form

    return render(request, 'register.html', context)

def vote(request, id):
    # 未登录用户不允许投票，自动跳回详情页
    if not isinstance(request.user, User):
        return redirect(to="detail", id=id)

    voter_id = request.user.id

    try:

        # 如果找不到登陆用户对此篇文章的操作，就报错
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_this_article.choice = request.POST["vote"]
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, article_id=id, choice=request.POST["vote"])
        new_ticket.save()

    # 如果是点赞，更新点赞总数
    if request.POST["vote"] == "like":
        article = Article.objects.get(id=id)
        article.likes += 1
        article.save()

    return redirect(to="detail", id=id)

def myinfo(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect(to='/index')
    context = {}
    if request.method == 'GET':
        try:
            sex = request.user.profile.sex
            ima = request.user.profile.profile_image

        except:
            sex = None
            ima = None
        context['sex'] = sex
        context['ima'] = ima
    elif request.method == 'POST':
        ch_id = request.user.id
        ch_user = User.objects.filter(id=ch_id)
        ch_user.username = request.POST.get('username')
        ch_user.profile_image = request.POST.get('pic')
        ch_user.sex = request.POST.get('sex')
        ch_user.password = request.POST.get('password')
        # print(username, sep=' ', end='n', file=sys.stdout, flush=False)
        # print(profile_image, sep=' ', end='n', file=sys.stdout, flush=False)
        # User.profile.save()
        User(id=ch_id, password=ch_user.password, name=ch_user.username, profile=UserProfile(sex=ch_user.sex, profile_image=ch_user.profile_image)).save()


    return render(request, 'myinfo.html', context=context, content_type=None, status=None, using=None)

def mycollection(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect(to='/index')
    context = {}
    article_list = Article.objects.all()
    user = request.user.id
    tk_list = Ticket.objects.all()
    tk_list = tk_list.filter(voter_id=user, choice='like')
    page_robot = Paginator(tk_list, 2, orphans=0, allow_empty_first_page=True)
    page_num = request.GET.get('page')
    try:
        tik_list = page_robot.page(page_num)
    except:
        tik_list = page_robot.page(1)
    context['tik_list'] = tik_list
    context['article_list'] = article_list
    context['page_num'] = page_num
    l = []
    for i in range(page_robot.num_pages):
        l.append(i+1)
    context['l'] = l
    return render(request, 'mycollection.html', context=context, content_type=None, status=None, using=None)
