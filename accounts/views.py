from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def register(requst):
    if requst.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=requst.POST)
        if form.is_valid():
            new_user = form.save()
            login(requst,new_user)
            return redirect('learning_logs:index')
    
    context = {"form":form}
    return render(requst, 'registration/register.html', context)

