from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _ 




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

    return render(request,'layouts/form.html',{'form':form})
