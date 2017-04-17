1. 上传图片
- models
FileField
- settings
MEDIA_URL = '/upload/'
MIDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
- urls
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

2. static
STATICFILES_DIRS=[]

3. templates
'DIRS': [os.path.join(BASE_DIR,'templates').replace('\\','/')],

4. create
django-admin startproject
python3 manage.py startapp

5. faker unreal data
from faker import Factory
fake = Factory.create()
for i in range(40):
     A = Article(
         title = fake.text(max_nb_chars=50),
         content = fake.text(max_nb_chars=500),
         img = f,
         # createtime = time.localtime()

     )
     A.save()

6. paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
page_robot = Paginator(article_list, 9)
article_list = page_robot.page(request.GET.get('page'))

try:
except EmptyPage:
except PageNotAnInteger:

7. login
from django.contrib.auth import authenticate, login

8. form
from django import forms
class CommentForm(forms.Form):
	forms.CharField

9. extend auth
-Models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile', on_delete=None, to_field=None)
    profile_image = models.FileField(verbose_name=None, name=None, upload_to='profile_image', storage=None)
-admin
register
-template
*/upload/*request.user.profile.profile_image

10. register and login
-view
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
def register_def(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    elif request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(to='login')
    context['form']=form
    return render(request, 'register.html', context=None, content_type=None, status=None, using=None)

11. logout
-urls
from django.contrib.auth.views import logout
url use logout as a exist view
suth as url(r'^logout/', logout, {'next_page':'register/'}, name='logout')

12. congratulate
-models  foreignkey + choices
class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile, on_delete=None, related_name='voted_tickets', related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True)
    article = models.ForeignKey(to=Article, on_delete=None, related_name='tickets', related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True)
    VOTE_CHOICES = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('normal', 'normal'),
    )
    choice = models.CharField(choices=VOTE_CHOICES, max_length=10)
-view
article = Article.objects.get(id=id)
like_counts = Ticket.objects.filter(choice='like', article_id=id).count()
try:
        voter_id = request.user.profile.id
        user_ticket_for_video = Ticket.objects.get(voter_id=voter_id, article_id=id)
        context['user_ticket'] = user_ticket_for_video

voter_id = request.user.profile.id
try:
        user_ticket_for_video = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_video.choice = request.POST['vote']
        user_ticket_for_video.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, video_id=id, choice=request.POST('vote'))
        new_ticket.save(force_insert=False, force_update=False, using=None, update_fields=None)
    return redirect(to='detail',id=id)
-template 
change the form

13. 
