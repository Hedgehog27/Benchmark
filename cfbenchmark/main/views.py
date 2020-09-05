from django.shortcuts import render, redirect, HttpResponse
from .codeforces import getDetail


def index(request):
    if request.method == 'GET':
        return render(request=request, template_name='main/index.html')
    if request.method == 'POST':
        username1 = request.POST.get('user1')
        username2 = request.POST.get('user2')
        detail = getDetail(username1, username2)
        return render(request=request, template_name='main/compare.html', context={'detail': detail})


def single(request):
    if request.method == 'GET':
        return render(request=request, template_name="main/single.html")
    if request.method == 'POST':
        username = request.POST.get('userid')
        return redirect('https://codeforces.com/profile/' + username)


def detail(request):
    if request.method == 'GET':
        return render(request=request, template_name="main/detail.html")
    else:
        return HttpResponse("Error 404: Page Not Found")


def about(request):
    if request.method == 'GET':
        return render(request=request, template_name="main/about.html")
    else:
        return HttpResponse("Error 404: Page Not Found")
