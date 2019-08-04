from django.shortcuts import render, redirect
from .forms import FormForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Forms, SubdivisionDetail


def trial(request):
    d = Forms.objects.all()
    context = {

        'display': d

    }
    return render(request, 'forms/trial.html', context)
