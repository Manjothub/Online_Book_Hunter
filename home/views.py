import re
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def INDEX(request):
    return render(request,'user/index.html')

def ADMIN_DASHBOARD(request):
    user = CustomUser.objects.get(id=request.user.id)
    context ={
        'user':user
    }
    return render(request,'admin/admin_dashboard.html',context)

def LOGINPAGE(request):
    return render(request,'common/login.html')

def DOLOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username=username, password=passw)
        if user is not None:
            login(request,user)
            user_type=user.user_type
            if user_type == '1':
                return redirect('dashboardadmin')
                # return HttpResponse('This is admin Pannel')
            elif user_type =='2':
                return HttpResponse('This is customer Pannel')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('loginpage')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('loginpage')
        
        
def DOLOGOUT(request):
    logout(request)
    return redirect('loginpage')


def CONTACT(request):
    return render(request,'user/contact.html')

def ADDBOOK (request):
    return render(request,'admin/add_book.html')