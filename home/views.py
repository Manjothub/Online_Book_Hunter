from django.shortcuts import render


def INDEX(request):
    return render(request,'user/index.html')
