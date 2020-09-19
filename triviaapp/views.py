from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from django.http import HttpResponseRedirect

from triviaapp.models import Game


def multiform(request):
    return render(request,'triviaapp/multiform.html')


def form_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse("multistepformexample"))
    else:
        name= request.POST.get("name")
        best_cricketer = request.POST.get("one")
        white= request.POST.get("white")
        yellow = request.POST.get("yellow")
        orange = request.POST.get("orange")
        green = request.POST.get("green")
        try:
            game = Game(name=name, best_cricketer=best_cricketer, white=white, yellow=yellow, orange=orange,
                        green=green)
            game.save()
            return HttpResponseRedirect('/')

        except Exception as e:
            print(e)
            return HttpResponseRedirect('/')


def home(request):
    qs = Game.objects.last()
    return render(request,'triviaapp/home.html',{"qs":qs})



def summary(request):
    qs= Game.objects.all()
    return render(request,'triviaapp/summary.html',{'qs':qs})



