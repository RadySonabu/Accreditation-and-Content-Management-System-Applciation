from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .admin import UserCreationForm
from django.http import HttpResponse
from .resources import Members
from .models import MyUser, College, Program
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# @login_required
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             employee_number = form.cleaned_data.get('employee_number')
#             messages.success(
#                 request, f'Account created for {employee_number}!')
#             return redirect('register')
#     else:
#         form = UserCreationForm()
#     return render(request, 'members/register.html', {'form': form})


@login_required
def export(request):
    member = Members()
    dataset = member.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="members.xls"'
    return response


def profile(request):
    return render(request, 'members/profile.html')


def load_college(request):
    role_id = request.GET.get('role')

    college = College.objects.filter(role_id=role_id)
    return render(request, 'members/college_dropdown_option.html', {'college': college, })


def load_program(request):
    college_id = request.GET.get('college')

    program = Program.objects.filter(college_id=college_id)
    return render(request, 'members/program_dropdown_option.html', {'program': program, })


class UserListView(LoginRequiredMixin, ListView):
    model = MyUser
    success_url = reverse_lazy('home')


class UserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MyUser

    form_class = UserCreationForm
    success_url = reverse_lazy('register')

    success_message = "%(account)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            account=f'{self.object.first_name} {self.object.last_name}',
        )


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = MyUser
    form_class = UserCreationForm
    success_url = reverse_lazy('user_changelist')
