from django.shortcuts import render,redirect
from .forms import  PostUpload
from .models import  Post,Category

from django.contrib import messages
from django.utils.translation import gettext_lazy as _
def index(request):
    list=Category.objects.all().order_by('-id')

    return render(request,'main/index.html' ,{'list':list})


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



