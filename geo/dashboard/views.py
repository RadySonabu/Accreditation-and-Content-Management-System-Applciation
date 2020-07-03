from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import LockscreenForm



@login_required
def home(request, *args, **kwargs):
    user = request.user
    context = {
       "user":user
    }

    return render(request, 'dashboard/home.html', context)

@login_required
def lockscreen(request):
   
    return render(request, 'dashboard/lockscreen.html')



