from django.shortcuts import render,redirect
from .forms import  PostUpload
def index(request):
    return render(request,'main/index.html',{})


def upload_post(request):
    if request.method=='POST':
        form=PostUpload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('main:upload')
    else:
        form=PostUpload()

    return  render(request,'layouts/form.html',{'form':form,'title':'Upload'})
