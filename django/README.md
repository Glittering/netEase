# django

#流程

##创建Django project
1. start project    
    django-admin startproject <name>
2. alter manage.py    
    *#!/usr/bin/ python3*
##创建Django App
1. start app    
    + python3 manage.py startapp <name>
    + python3 manage.py <command> [options]
2. setting 
    添加上'<jangoappname>'
##数据库
1. 合并/运行数据库
    + python3 manage.py makemigrations
    + python3 manage.py migrate
2. run server
    + python3 manage.py runserver
##创建数据表
1. models.py中定义一个类和相对应的数据字段
    + class People(models.Model):
        - name = models.CharField(null=True,blank=True,max_length=200)
	- null --> 可以没有
	- blank --> 可以为空
	- max_length --> 最大长度
2. 合并数据库
    + 同 数据库 1.  
    + **每次model改动，都需要合并**
##view中获取model
1. 在view创建视图函数
    + from firstapp.models import People
    + def name(request):
##引入Template对数据渲染
1. 引入template
    + from django.template import Context,Template
    + from django.shortcuts import render,HttpResponse
    + t=Template(html)
    + c=Context({'person': person})
    + web_page=t.render(c)
    + return HttpResponse(web_page)
##URL中分配网址
1. 添加URL
    + from firstapp.views import first_try
    + url(r'^first_try',first_try),



#2017年 03月 22日 星期三 10:53:48 CST
##django项目实战
1. 创建模板
    + 修改setting
    + 静态文件标签
2. 后台
    + createsuperuser
    + admin 中注册数据库   admin.site.register()
    + model 中添加__str__方法
3. model中引入数据
    + Class.objects.all()
    + render(request, 'webname', context)
4. jango模板语言
    + {% %}
    + {{ }}


#2017年 03月 23日 星期四 10:14:17 CST
##Get文章分类
*Time Will Tell*
###model
1. model 添加tag字段，CharField参数choices=两重元组
###View
2. request.GET   META   POST
request.GET.get('tag')
3. if queryset:   else
Aritcle.objects.filter(tag=queryset)
4. html中
a 的href  ?tag=... 
##QuerySet
###迭代  all()
###存在  exists()
###求值  repr()  len()  list()  bool()
###筛选方法
1. **filter()**
2. exclude()
3. annotate()
4. **order_by()**   desc()  asc()
5. reverse()
6. distinct()  去除重复的行
7. values()
8. datetimes()
9. none()
10. all()
11. select_related()
12. prefetch_related()
13. extra()
14. 
.......

#2017年 03月 24日 星期五 12:05:31 CST
##post
1. 快速部署
2. 渲染表单
+ form django import forms
+ class CommentForm(forms.Form):
+ as_p
3. 绑定表单&& 返回校验结果  数据分离
+ CommentForm(request.POST)
+ csrf_token
+ form   and   form.errors
4. 数据存储
+ is_valid()
+ form.cleaned_data[''] form中存储数据的地
+ redirect()  重定向
5. 定制表单的验证逻辑
+ forms.CharField(widget=forms.Textareai(attrs={'class':'abc'}))  attrs最好不要有
+ error_message={}   
    - 'required':'' 空参数   
    - 'invaild'
+ validators={}
+ from django.core.exception import ValidationError
+ raise
6. 表单的手工渲染
div class=field
{{field.label}}
{{field}}
{{field.errors|yesno:'error, '}}


#2017年 04月 06日 星期四 19:13:32 CST
1. url
- (?P<page_num>\d+)  从url获取数字
- (?P<page_num>\d+)/comment  试表分离
- views 中获取参数，用get分离文章

2. 评论
- models 中加ForeignKey(to, related_name)
- best_comment BooleanField(default)
- templates 中 用 article.under_comments.all

3. 一图多表
- url 分离
- view中 form和 comment分离
- valid失败后返回error
- detail中 判断error


#2017年 04月 07日 星期五 18:34:28 CST
1. STATICFILES_DIRS
2. MEDIA_ROOT

#Something others
##过滤器  {{article.conent|truncatewords:100}}
##date    article.date|date:'Y-m-d'
