from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm
from django.http import HttpResponse
from .resources import Members
from .models import MyUser


@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            employee_number = form.cleaned_data.get('employee_number')
            messages.success(
                request, f'Account created for {employee_number}!')
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'members/register.html', {'form': form})


@login_required
def export(request):
    member = Members()
    dataset = member.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="members.xls"'
    return response


def display_all_dean(request):

    context = {
        'dean': MyUser.objects.all()
    }

    return render(request, 'members/home.html', context)
