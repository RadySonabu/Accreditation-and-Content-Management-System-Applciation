from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from members.models import MyUser
from forms.models import Forms


def home(request):
    user = request.user
    if user.is_authenticated and user.role.role == 'VPAA':
        context = {
            'members': MyUser.objects.filter(role__role='DEAN')
        }
    elif user.is_authenticated and user.role.role == 'DEAN':
        if user.college.college == 'CITE':

            context = {
                'members': MyUser.objects.filter(role__role='DEPTCHAIR', college__college='CITE')
            }
        else:

            context = {
                'members': MyUser.objects.filter(role__role='DEPTCHAIR')
            }
    elif user.is_authenticated and user.role.role == 'DEPTCHAIR':
        if user.program.program == 'BSIT':

            context = {
                'members': MyUser.objects.filter(program__program='BSIT'),
                'form': Forms.objects.all()
            }
    else:
        return render(request, 'dashboard/home.html')

    return render(request, 'dashboard/home.html', context)
