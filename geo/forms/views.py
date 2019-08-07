from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.http import HttpResponse
from .models import Forms, SubdivisionDetail, Subdivision, Division
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class FormListView(ListView):
    model = Forms
    context_object_name = 'forms'


class FormDetailView(DetailView):

    model = Forms
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()
        return context


class FormCreateView(CreateView):
    model = Forms

    fields = "__all__"
    success_url = '/form/'


class FormUpdateView(UpdateView):
    model = Forms
    fields = "__all__"
    success_url = '/form/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()
        return context


class FormDeleteView(DeleteView):
    model = Forms
    success_url = '/form/'
# ----------------------------------------------------------------------------------


class DivisionListView(ListView):
    model = Division
    context_object_name = 'forms'


class DivisionDetailView(DetailView):
    model = Division
    fields = "__all__"


class DivisionCreateView(CreateView):
    model = Division
    fields = "__all__"
    success_url = '/division/'


class DivisionUpdateView(UpdateView):
    model = Division
    fields = "__all__"
    success_url = '/division/'


class DivisionDeleteView(DeleteView):
    model = Division
    success_url = '/division/'
# ----------------------------------------------------------------------------------


class SubdivisionListView(ListView):
    model = Subdivision
    context_object_name = 'forms'


class SubdivisionDetailView(DetailView):
    model = Subdivision
    fields = "__all__"


class SubdivisionCreateView(CreateView):
    model = Subdivision
    fields = "__all__"
    success_url = '/subdivision/'


class SubdivisionUpdateView(UpdateView):
    model = Subdivision
    fields = "__all__"
    success_url = '/subdivision/'


class SubdivisionDeleteView(DeleteView):
    model = Subdivision
    success_url = '/subdivision/'


# -----------------------------------------
class SubdivisionDetailListView(ListView):
    model = SubdivisionDetail
    context_object_name = 'forms'


class SubdivisionDetailDetailView(DetailView):
    model = SubdivisionDetail


class SubdivisionDetailCreateView(CreateView):
    model = SubdivisionDetail
    fields = "__all__"
    success_url = '/subdivisiondetail/'


class SubdivisionDetailUpdateView(UpdateView):
    model = SubdivisionDetail
    fields = "__all__"
    success_url = '/subdivisiondetail/'


class SubdivisionDetailDeleteView(DeleteView):
    model = SubdivisionDetail
    success_url = '/subdivisiondetail/'
