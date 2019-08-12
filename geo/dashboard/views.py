from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from members.models import MyUser


def home(request):
    user = request.user
    if user.is_authenticated and user.role == 'VPAA':
        context = {
            'members': MyUser.objects.filter(role='Dean')
        }
    elif user.is_authenticated and user.role == 'Dean':
        if user.college == 'CITE':

            context = {
                'members': MyUser.objects.filter(role='DEPTCHAIR', college='CITE')
            }
        else:

            context = {
                'members': MyUser.objects.filter(role='DEPTCHAIR')
            }
    elif user.is_authenticated and user.role == 'DEPTCHAIR':
        if user.program == 'BSIT':

            context = {
                'members': MyUser.objects.filter(program='BSIT')

            }
    else:
        return render(request, 'dashboard/home.html')

    return render(request, 'dashboard/home.html', context)
