from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from members.models import MyUser
from forms.models import Forms, AccreditationType, Division, Subdivision, SubdivisionDetail, Files
from .forms import LockscreenForm
from forms.forms import FormForm


@login_required
def home(request):
    user = request.user
    if user.is_authenticated and user.role.role == 'VPAA':
        year_js = request.GET.get('year') or 2019
        print(year_js)
        year_str = str(year_js)
        year = int(year_str)
        print(type(year))
        if year == 2019:
            context = {
                'members': MyUser.objects.filter(role__role='COLLEGE DEAN'),
                'accr_type': AccreditationType.objects.all(),
                'title': 'Home',
                'f': Forms.objects.all(),
                'user': user,
                'year': year,
            }
            return render(request, 'dashboard/home.html', context)
    elif user.is_authenticated and user.role.role == 'COLLEGE DEAN':
        # if user.college.college == 'College of Information Technology Education':
        year_js = request.GET.get('year') or 2019
        print(year_js)
        year_str = str(year_js)
        year = int(year_str)
        print(type(year))
        files = Files.objects.exclude(note_from_auditor='')
        count = files.count()
        messages.info(request, f'You have {count} notes left')
        if year == 2019:
            context = {
                'members': MyUser.objects.filter(program__program='BS Information Technology'),
                'accr_type': AccreditationType.objects.all(),
                'title': 'Home',
                'f': Forms.objects.all(),
                'user': user,
                'year': year,


            }
            return render(request, 'dashboard/home.html', context)

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


@login_required
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


@login_required
def lockscreen(request):
    # form = LockscreenForm
    # password1 = self.cleaned_data.get("password1")
    # password2 = self.cleaned_data.get("password2")
    # if password1 and password2 and password1 != password2:
    #     raise forms.ValidationError("Passwords don't match")
    # if form.is_valid():
    #     return render(request, 'dashboard/home.html')
    return render(request, 'dashboard/lockscreen.html')


def detail_form(request, *args, **kwargs):
    context = {
        'form': FormForm,
        'f': Forms.objects.all(),
        'd': Division.objects.all(),
        'sd': Subdivision.objects.all(),
        'sdd': SubdivisionDetail.objects.all(),
        'pk': kwargs.get('pk')
    }
    return render(request, 'dashboard/detailed_form.html', context)
