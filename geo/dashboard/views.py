from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from members.models import MyUser
from forms.models import Forms, AccreditationType


@login_required
def home(request):
    user = request.user
    if user.is_authenticated and user.role.role == 'VPAA':
        context = {
            'members': MyUser.objects.filter(role__role='COLLEGE DEAN')
        }
    elif user.is_authenticated and user.role.role == 'COLLEGE DEAN':
        # if user.college.college == 'College of Information Technology Education':
        year_js = request.GET.get('year') or 2019
        print(year_js)
        year_str = str(year_js)
        year = int(year_str)
        print(type(year))
        if year == 2019:
            context = {
                'members': MyUser.objects.filter(program__program='BS Information Technology'),
                'accr_type': AccreditationType.objects.all(),
                'title': 'Home',
                'f': Forms.objects.all(),
                'user': user,
                'year': year

            }
            return render(request, 'dashboard/home.html', context)
        # else:

        #     context = {
        #         'members': MyUser.objects.filter(role__role='DEPARTMENT CHAIRPERSON')
        #     }
    elif user.is_authenticated and user.role.role == 'DEPARTMENT CHAIRPERSON':
        if user.program.program == 'BS Information Technology':

            context = {
                'members': MyUser.objects.filter(program__program='BS Information Technology'),
                'accr_type': AccreditationType.objects.all(),
                'title': 'Home',
                'f': Forms.objects.all(),

            }
    else:
        context = {
            'y': "Hello"
        }
        return render(request, 'dashboard/home.html', context)

    return render(request, 'dashboard/home.html', context)


@login_required
def calendar(request):
    return render(request, 'dashboard/calendar.html', {'title': 'Calendar'})


@login_required
def chairperson_forms(request, pk):
    user = request.user
    if user.program.program == 'BS Information Technology':
        context = {
            'members': MyUser.objects.filter(program__program='BS Information Technology'),
            'accr_type': AccreditationType.objects.all(),
            'title': 'Home',
            'f': Forms.objects.all(),
            'pk': pk
        }
    else:
        return render(request, 'dashboard/home.html')
    return render(request, 'forms/chairperson_forms.html', context)


def form_year(request):
    year_js = request.GET.get('year') or 2019
    print(year_js)
    year_str = str(year_js)
    year = int(year_str)
    print(type(year))
    context = {
        'members': MyUser.objects.filter(program__program='BS Information Technology'),
        'accr_type': AccreditationType.objects.all(),
        'title': 'Home',
        'f': Forms.objects.all(),
        'user': user,
        'year': year

    }
    return render(request, 'forms/load_forms.html', context)


def lockscreen(request):
    return render(request, 'dashboard/lockscreen.html')
