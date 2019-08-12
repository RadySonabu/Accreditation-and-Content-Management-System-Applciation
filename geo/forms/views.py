from django import forms

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.http import HttpResponse
from .models import Forms, SubdivisionDetail, Subdivision, Division
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import SubdivisionForm, SubdivisionDetailForm

from django.forms.models import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin


class FormListView(LoginRequiredMixin, ListView):
    model = Forms
    context_object_name = 'forms'


class FormDetailView(LoginRequiredMixin, DetailView):

    model = Forms
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()
        return context


class FormCreateView(LoginRequiredMixin, CreateView):
    model = Forms

    fields = "__all__"
    success_url = '/form/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()
        return context


class FormUpdateView(LoginRequiredMixin, UpdateView):
    model = Forms
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class FormDeleteView(LoginRequiredMixin, DeleteView):
    model = Forms
    success_url = '/form/'
# ----------------------------------------------------------------------------------


class DivisionListView(LoginRequiredMixin, ListView):
    model = Division
    context_object_name = 'forms'


class DivisionDetailView(LoginRequiredMixin, DetailView):
    model = Division
    fields = "__all__"
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionCreateView(LoginRequiredMixin, CreateView):
    model = Division
    fields = "__all__"

    def form_valid(self, form):

        form.instance.title_id = self.kwargs.get('pk')

        print(self)

        return super(DivisionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionUpdateView(LoginRequiredMixin, UpdateView):
    model = Division
    fields = ['criteria', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionDeleteView(LoginRequiredMixin, DeleteView):
    model = Division

    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse_lazy('form-detail', kwargs={'pk': self.object.title.id})


# ----------------------------------------------------------------------------------


class SubdivisionListView(LoginRequiredMixin, ListView):
    model = Subdivision
    context_object_name = 'forms'


class SubdivisionDetailView(LoginRequiredMixin, DetailView):
    model = Subdivision
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionCreateView(LoginRequiredMixin, CreateView):
    model = Subdivision

    form_class = SubdivisionForm

    def form_valid(self, form):

        form.instance.division_id = self.kwargs.get('pk')

        print(self)

        return super(SubdivisionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionUpdateView(LoginRequiredMixin, UpdateView):
    model = Subdivision

    form_class = SubdivisionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDeleteView(LoginRequiredMixin, DeleteView):
    model = Subdivision

    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse_lazy('form-detail', kwargs={'pk': self.object.division.title.id})
# -----------------------------------------


class SubdivisionDetailListView(LoginRequiredMixin, ListView):
    model = SubdivisionDetail
    context_object_name = 'forms'


class SubdivisionDetailDetailView(LoginRequiredMixin, DetailView):
    model = SubdivisionDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDetailCreateView(LoginRequiredMixin, CreateView):
    model = SubdivisionDetail
    fields = "__all__"

    def form_valid(self, form):

        form.instance.subdivision_id = self.kwargs.get('pk')

        print(self)

        return super(SubdivisionDetailCreateView, self).form_valid(form)


class SubdivisionDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = SubdivisionDetail
    form_class = SubdivisionDetailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDetailDeleteView(LoginRequiredMixin, DeleteView):
    model = SubdivisionDetail

    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse_lazy('form-detail', kwargs={'pk': self.object.subdivision.division.title.id})
