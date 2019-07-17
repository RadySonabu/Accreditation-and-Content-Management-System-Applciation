from django.shortcuts import render


from members.models import MyUser


def home(request):

    context = {
        'members': MyUser.objects.filter(course='Dean')
    }

    return render(request, 'dashboard/home.html', context)
