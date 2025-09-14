from django.shortcuts import render,redirect
from .forms import  PostUpload
from .models import  Post,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


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



