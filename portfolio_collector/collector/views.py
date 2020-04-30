from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import *
def main(request):
    return render(request,'main.html')


def registration(request):
    if  request.user.is_authenticated == False:
        if request.method == "POST":   
            name = request.POST['login']
            password1 = request.POST['password']
            password2 = request.POST['password1']
            if len(User.objects.filter(username=name)) > 0:
                messages.error(request, 'Такой пользователь уже существует')
                return render(request,'registration.html')
            if password1==password2:
                User.objects.create_user(username = name,password = password1)
                return redirect('/sign_in')
            elif password1!=password2:
                messages.error(request, 'Пароли отличаются друг от друга')
                return render(request,'registration.html')
        if request.method == "GET":
            return render(request,'registration.html')
    else:
        return redirect('/main.html')
def log_in(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')


def create_portfolio(request):
    if request.user.is_authenticated == True:
        portfolios = Portfolio.objects
        deliting = Portfolio.objects.filter(author_id = request.user.id)
        deliting.delete()
        city = request.POST.get('city')
        profession = request.POST.get('profession')
        experience = request.POST.get('experience')
        if str(experience).isdigit() == True:
            pass
        else:
            experience = 0
        full_name = request.POST.get('full_name')
        education = request.POST.get('education')
        discription = request.POST.get('discription')
        
        portfolios.create(author_full_name = full_name,author_id = request.user.id,city=city,profession=profession,
        experience=experience,education=education,discription=discription)
        print(city,profession,experience,full_name,education,discription)
        return render(request,'portfolio.html')
    else:
        return redirect('/log_in')
def show_profile(request):
    if request.user.is_authenticated:

        context={}
        profiles = Portfolio.objects.filter(author_id = request.user.id)
        for i in profiles:
            context={'city':i.city,'profession':i.profession,
            'experience':i.experience,'education':i.education
            ,'discription':i.discription,'full_name':i.author_full_name}
        return render(request,'profile.html',context)
    else:
        return redirect('/sign_in')
def show_user(request,id):
    if request.user.is_authenticated:

        context={}
        profiles = Portfolio.objects.filter(author_id = id)
        for i in profiles:
            context={'city':i.city,'profession':i.profession,
            'experience':i.experience,'education':i.education
            ,'discription':i.discription,'full_name':i.author_full_name}
        return render(request,'profile.html',context)
    else:
        return redirect('/sign_in')
def show_list(request):
    if request.user.is_authenticated:
        experience = request.POST.get('experience')
        profession = request.POST.get('profession')
        workers = Portfolio.objects.filter(experience = experience, profession=profession)
        context={'workers':workers}
        return render(request,'lenta.html',context)
    else:
        return redirect('/log_in')
