from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.http import HttpResponse
from .models import Forms, SubdivisionDetail, Subdivision, Division
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import SubdivisionForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()
        return context


class FormUpdateView(UpdateView):
    model = Forms
    fields = "__all__"

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
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionCreateView(CreateView):
    model = Division
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionUpdateView(UpdateView):
    model = Division
    fields = "__all__"


class DivisionDeleteView(DeleteView):
    model = Division

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


class SubdivisionUpdateView(UpdateView):
    model = Subdivision
    fields = "__all__"


class SubdivisionDeleteView(DeleteView):
    model = Subdivision


# -----------------------------------------
class SubdivisionDetailListView(ListView):
    model = SubdivisionDetail
    context_object_name = 'forms'


class SubdivisionDetailDetailView(DetailView):
    model = SubdivisionDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDetailCreateView(CreateView):
    model = SubdivisionDetail
    fields = "__all__"


class SubdivisionDetailUpdateView(UpdateView):
    model = SubdivisionDetail
    fields = "__all__"

    def subdivision_value(self):
        pass


class SubdivisionDetailDeleteView(DeleteView):
    model = SubdivisionDetail
