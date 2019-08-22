from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from members.models import MyUser
from forms.models import Forms


@login_required
def home(request):
    user = request.user
    if user.is_authenticated and user.role.role == 'VPAA':
        context = {
            'members': MyUser.objects.filter(role__role='COLLEGE DEAN')
        }
    elif user.is_authenticated and user.role.role == 'COLLEGE DEAN':
        if user.college.college == 'College of Information Technology Education':

            context = {

                'members': MyUser.objects.filter(role__role='DEPARTMENT CHAIRPERSON', college__college='College of Information Technology Education')
            }
        else:

            context = {
                'members': MyUser.objects.filter(role__role='DEPARTMENT CHAIRPERSON')
            }
    elif user.is_authenticated and user.role.role == 'DEPARTMENT CHAIRPERSON':
        if user.program.program == 'BS Information Technology':

            context = {
                'members': MyUser.objects.filter(program__program='BS Information Technology'),
                'form': Forms.objects.all()
            }
    else:
        return render(request, 'dashboard/home.html')

    return render(request, 'dashboard/home.html', context)
