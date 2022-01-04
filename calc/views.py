from django.shortcuts import render
import random
from django.contrib.auth.models import User, AnonymousUser
from datetime import datetime, date
from .models import Adding, Star
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect

startTime = datetime.now()
li = [1, 2]
correct_ans = []
wrong_ans = []
reslist = []
rightimage = [
    "https://st4.depositphotos.com/5624298/22256/i/600/depositphotos_222567662-stock-photo-words-well-done-written-colorful.jpg",
    "https://thumbs.gfycat.com/AcademicMadGoshawk-size_restricted.gif",
    "https://media1.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif",
    

]

wrongimage = [
    "https://cdn.imgbin.com/22/25/0/imgbin-youtube-google-play-avatar-google-search-wow-face-iSK2PpedNqRBfeLNhuykTK4em.jpg",
    "https://i.pinimg.com/736x/ff/5d/2b/ff5d2b82844234edc2115ed9102f8cc4.jpg",


]
# Create your views here.

def timereset():
    global startTime, correct_ans, wrong_ans
    startTime = datetime.now()
    correct_ans = []
    wrong_ans = []  


def add(request):
    
    timing = "Start again"
    num1 = random.randint(0,6)
    num2 = random.randint(0,6)
    res = num1 + num2
    li.append(res)
    form = request.POST.get("value")

    left =  str(12 - (len(li)))
    
    if str(form) == str(li[-2]):
        correct_ans.append("v")
        
    else:
        wrong_ans.append("x")

    
    if len(li) == 12:
        endTime = datetime.now()
        timing = endTime - startTime
        del li[0:10]
        
        if request.user.is_authenticated:
            add = Adding(time=str(timing), correct = str(len(correct_ans)), wrong=str(len(wrong_ans)),user=request.user)
            add.save()
            if len(correct_ans) == 10:
                count = Star(add=(1), user=request.user)
                count.save()

            
            
        else:
            timereset()
        timereset()

    context = {
        "form":form, 
        "num1":num1, 
        "num2":num2, 
        "res":res, 
        "li":str(li[-2]),
        "timing" : timing,
        "left" : left,
        "right_image" : random.choice(rightimage),
        "wrong_image" : random.choice(wrongimage),
        "correct" : str(len(correct_ans)),
        "wrong" : str(len(wrong_ans)),
        
                
        }
    if request.user.is_authenticated:
        starcount = Star.objects.filter(add=(1), user=request.user).count
        starcount = {"count":starcount}
        context.update(starcount) 
    return render(request, 'calc/add.html', context)




def sub(request):
    
    timing = "Start again"
    num1 = random.randint(1,10)
    num2 = random.randint(1,5)
    a = 0 #1
    b = 0 #5
    
    if num1>num2:
        res = num1 - num2
    else:
        a = num1 #1
        b = num2 #5
        num1 = b
        num2 = a
        res = num1 - num2
    
    li.append(res)
    form = request.POST.get("value")

    left =  str(12 - (len(li)))
    
    if str(form) == str(li[-2]):
        correct_ans.append("v")
        
    else:
        wrong_ans.append("x")

    
    if len(li) == 12:
        endTime = datetime.now()
        timing = endTime - startTime
        del li[0:10]
        
        if request.user.is_authenticated:
            add = Adding(time=str(timing), correct = str(len(correct_ans)), wrong=str(len(wrong_ans)),user=request.user)
            add.save()
            if len(correct_ans) == 10:
                count = Star(sub=(1), user=request.user)
                count.save()
        else:
            timereset()
        timereset()

    context = {
        "form":form, 
        "num1":num1, 
        "num2":num2, 
        "res":res, 
        "li":str(li[-2]),
        "timing" : timing,
        "left" : left,
        "right_image" : random.choice(rightimage),
        "wrong_image" : random.choice(wrongimage),
        "correct" : str(len(correct_ans)),
        "wrong" : str(len(wrong_ans))

        
        }
    if request.user.is_authenticated:
        starcount = Star.objects.filter(sub=(1), user=request.user).count
        starcount = {"count":starcount}
        context.update(starcount) 
   
    return render(request, 'calc/substraction.html', context)


rand_5 = [2,5,10]
def mul(request):
    timing = "Start again"
    num1 = random.choice(rand_5)
    num2 = random.randint(1,12)
    res = num1 * num2
    li.append(res)
    form = request.POST.get("value")

    left =  str(12 - (len(li)))
    if str(form) == str(li[-2]):
        correct_ans.append("v")
        
    else:
        wrong_ans.append("x")

    
    if len(li) == 12:
        endTime = datetime.now()
        timing = endTime - startTime
        del li[0:10]

        if request.user.is_authenticated:
            add = Adding(time=str(timing), correct = str(len(correct_ans)), wrong=str(len(wrong_ans)),user=request.user)
            add.save()
            if len(correct_ans) == 10:
                count = Star(mul=(1), user=request.user)
                count.save()
        else:
            timereset()
        timereset()

    context = {
        "form":form, 
        "num1":num1, 
        "num2":num2, 
        "res":res, 
        "li":str(li[-2]),
        "timing" : timing,
        "left" : left,
        "right_image" : random.choice(rightimage),
        "wrong_image" : random.choice(wrongimage),
        "correct" : str(len(correct_ans)),
        "wrong" : str(len(wrong_ans))

        
        }
    if request.user.is_authenticated:
        starcount = Star.objects.filter(mul=(1), user=request.user).count
        starcount = {"count":starcount}
        context.update(starcount) 
   
        
    return render(request, 'calc/mul.html', context)


color = ["red","black","blue","yellow"]
color1 = ["white","green","blue","orange"]
def index(request):
    coloring = random.choices(color)
    coloring = str(coloring)
    coloring = coloring.strip("['']")

    coloring1 = random.choices(color1)
    coloring1 = str(coloring1)
    coloring1 = coloring1.strip("['']")
    context = {"color": coloring, "color1": coloring1}
    
    return render(request, 'calc/index.html', context)



def userstars(request):
    add = Star.objects.filter(user=request.user, add=1).count
    sub = Star.objects.filter(user=request.user, sub=1).count
    mul = Star.objects.filter(user=request.user, mul=1).count
    

    context = {"sub":sub, "add":add, "mul":mul}
    return render(request, "calc/userstars.html", context)

