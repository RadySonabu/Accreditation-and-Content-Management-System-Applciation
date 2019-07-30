from django.shortcuts import render, redirect
from .forms import CreateForm_FORMs
from django.contrib import messages
from django.http import HttpResponse

def EditFormView(request):
    if request.method == 'POST':
        form = CreateForm_FORMs(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('create_form')
    else:
        form = CreateForm_FORMs()
    return render(request, 'forms/create_form.html', {'form': form})