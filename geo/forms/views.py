from django.shortcuts import render, redirect
from .forms import CoE_IT_FORM_FORMs
from django.contrib import messages
from django.http import HttpResponse

def EditFormView(request):
    if request.method == 'POST':
        form = CoE_IT_FORM_FORMs(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('forms')
    else:
        form = CoE_IT_FORM_FORMs()
    return render(request, 'forms/forms.html', {'form': form})
