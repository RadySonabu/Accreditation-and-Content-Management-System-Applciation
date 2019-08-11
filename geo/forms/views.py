from django import forms

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.http import HttpResponse
from .models import Forms, SubdivisionDetail, Subdivision, Division
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import SubdivisionForm, SubdivisionDetailForm

from django.forms.models import modelform_factory


class FormListView(ListView):
    model = Forms
    context_object_name = 'forms'


class FormDetailView(DetailView):

    model = Forms
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
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

    def form_valid(self, form, ):
        title = form.save(commit=True)
        title

        return super(DivisionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionUpdateView(UpdateView):
    model = Division
    fields = ['criteria', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionDeleteView(DeleteView):
    model = Division

    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse_lazy('form-detail', kwargs={'pk': self.object.title.id})


# ----------------------------------------------------------------------------------


class SubdivisionListView(ListView):
    model = Subdivision
    context_object_name = 'forms'


class SubdivisionDetailView(DetailView):
    model = Subdivision
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionCreateView(CreateView):
    model = Subdivision

    form_class = SubdivisionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionUpdateView(UpdateView):
    model = Subdivision

    form_class = SubdivisionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDeleteView(DeleteView):
    model = Subdivision

    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse_lazy('form-detail', kwargs={'pk': self.object.division.title.id})
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
    form_class = SubdivisionDetailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDetailDeleteView(DeleteView):
    model = SubdivisionDetail

    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse_lazy('form-detail', kwargs={'pk': self.object.subdivision.division.title.id})
