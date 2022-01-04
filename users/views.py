from django.shortcuts import render, redirect

# Create your views here.
from .forms import NewUser

def register(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewUser()
    return render(request, 'users/register.html', {"form":form})