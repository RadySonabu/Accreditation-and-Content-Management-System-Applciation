from django.shortcuts import render


from members.models import MyUser


def home(request):
    user = request.user
    if user.course == 'VPAA':
        context = {
            'members': MyUser.objects.filter(course='Dean')
        }
    elif user.course == 'Dean':
        context = {
            'members': MyUser.objects.filter(course='DC')
        }
    elif user.course == 'DC':
        context = {

        }
    else:
        f'Non admin'
    return render(request, 'dashboard/home.html', context)
