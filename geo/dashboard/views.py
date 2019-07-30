from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from members.models import MyUser


def home(request):
    user = request.user
    if user.is_authenticated and user.course == 'VPAA':
        context = {
            'members': MyUser.objects.filter(course='Dean')
        }
    elif user.is_authenticated and user.course == 'Dean':
        if user.college =='CITE':

            context = {
                'members': MyUser.objects.filter(course='DC', college='CITE')
            }
        else:

            context = {
                'members': MyUser.objects.filter(course='DC')
            }
    elif user.is_authenticated and user.course == 'DC':
        if user.program == 'BSIT':

            context = {
                'members': MyUser.objects.filter(program='BSIT')
                
            }
    else: 
        return render(request, 'dashboard/home.html')
        
        

    return render(request, 'dashboard/home.html', context)
