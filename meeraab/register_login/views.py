from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def register_login(request):
    form = CreateUserForm()
    if(len(request.POST) == 3):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, "نام‌کاربری یا رمز عبور اشتباه است!")
            return redirect('register_login:register_login')
    elif(len(request.POST) == 4):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, username + ' کاربر جدید با موفقیت اضافه شد! ' )
            return redirect('register_login:register_login')
        else:
            messages.info(request, "نام‌کاربری و یا رمزعبور مناسب انتخاب نشده‌است!")

    context={'form':form}
    return render(request,"register_login/register_login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('/')
