from django.shortcuts import get_object_or_404, render,redirect
from django.urls import is_valid_path, reverse
from .forms import RegistrationForm,LoginForm,ProfileForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import User




def create_post(request):
    title=_("Ro'yxatdan o'tish")
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request,_("Siz muvaffiqiyatli ro'yxatdan o'tdingiz" ))
            return redirect('main:index')
    else:
        form=RegistrationForm()

    return render(request,'layouts/form.html',{'form':form,'title':title})
def user_login(request):
    title=_('Tizimga kirish')
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if not user is None:
                login(request,user)
                messages.success(request,_('Xush kelibsiz,{}'.format(user.username)))

                return redirect('main:index')
            else:
                form.add_error(None,_('Login xato '))

    else:
        form=LoginForm()

    return render(request,'layouts/form.html',{'form':form,'title':title})

@login_required
def client_logout(request):
    messages.success(request,'Xayr {}'.format(request.user.username))
    logout(request)
    return redirect('main:index')


def profile_update(request):


    if request.method=='POST':
        form=ProfileForm(data=request.POST,files=request.FILES,instance=request.user)
        if form.is_valid():
            form.save() 
            return redirect('client:profile')
    else:
        form=ProfileForm(instance=request.user)

    ctx={
        'form':form,
        'title':'Profile',
        'button_title':'Chiqish'

    }
    return render(request,'layouts/form.html',ctx)



