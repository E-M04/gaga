from django.shortcuts import render,redirect, get_object_or_404
from .forms import  PostUpload
from django.db import transaction
from .models import  Post,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import Http404

def index(request):
    post=Post.objects.all()
    paginator=Paginator(Post.objects.all(),1)
    page= request.GET.get('page')
    posts=paginator.get_page(page)
    nums='a'*posts.paginator.num_pages
    ctx={
        
        'list':Category.objects.all().order_by('-id'),
        'post':post,
        'posts':posts,
        'nums':nums
        
         }

    return render(request,'main/index.html' ,ctx)


def upload_post(request):
    if request.method=='POST':
        form=PostUpload(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            messages.success(request, _("Muvaffaqiyatli qo'shildi."))
            return  redirect('main:upload')
    else:
        form=PostUpload()

    return  render(request,'layouts/form.html',{'form':form,'title':'Upload'})


#For like and dislike 


def post_like(request,post_id,action):
    if action not in ['like', 'dislike']:
        raise Http404
    
    def _redirect():
        return redirect(request.GET.get('return','main:index'))
    
    with transaction.atomic():
        try:
            post=Post.objects.select_for_update().get(id=post_id)
        except Post.DoesNotExist:
            return _redirect()
        

        if action=='like':
            post.like+=1
        else:
            post.dislike+=1
        post.save()


        return _redirect()