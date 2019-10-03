from django import forms

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import SubdivisionForm, SubdivisionDetailForm, FormForm, FileForm, DivisionForm
from .models import Files

from django.forms.models import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Sum, Avg, F
from forms.models import Forms, SubdivisionDetail, Subdivision, Division, AccreditationType
from django.db.models.expressions import RawSQL
from django.db import IntegrityError

from django.core.files.storage import FileSystemStorage


class FormListView(LoginRequiredMixin, ListView):
    model = Forms
    context_object_name = 'forms'
    def form_valid(self, form):

        form.instance.id = self.kwargs.get('pk')

        return super(FormListView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = 2019
        context['a'] = self.kwargs.get('pk')
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class FormDetailView(LoginRequiredMixin, DetailView):

    model = Forms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()
        return context


class FormCreateView(LoginRequiredMixin, CreateView):
    model = Forms
    form_class = FormForm

    error_message = "%(account)s is already created!"

    def form_valid(self, form):

        form.instance.created_by = self.request.user
        self.kwargs.get('pk')

        form.instance.title = f'{form.instance.type_of_accreditation} {form.instance.created_for} {form.instance.year}'
        title = Forms.objects.filter(
            title=f'{form.instance.type_of_accreditation} {form.instance.created_for} {form.instance.year}')
        if not title:
            form.instance.college = self.request.user.college
        else:

            return redirect('form-detail')
        return super(FormCreateView, self).form_valid(form)

    def get_error_message(self, cleaned_data):
        return self.error_message % dict(
            cleaned_data,
            account=f'{self.object.title} Title!',
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['a'] = self.kwargs.get('pk')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context
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
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class DivisionCreateView(LoginRequiredMixin, CreateView):
    model = Division
    form_class = DivisionForm

    def form_valid(self, form):

        form.instance.title_id = self.kwargs.get('pk')

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
    form_class = DivisionForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context

# ----------------------------------------------------------------------------------


class SubdivisionListView(LoginRequiredMixin, ListView):
    model = Subdivision
    context_object_name = 'forms'


class SubdivisionDetailView(LoginRequiredMixin, DetailView):
    model = Subdivision
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionCreateView(LoginRequiredMixin, CreateView):
    model = Subdivision

    form_class = SubdivisionForm

    def form_valid(self, form):

        form.instance.division_id = self.kwargs.get('pk')

        return super(SubdivisionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionUpdateView(LoginRequiredMixin, UpdateView):
    model = Subdivision

    form_class = SubdivisionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context
# -----------------------------------------


class SubdivisionDetailListView(LoginRequiredMixin, ListView):
    model = SubdivisionDetail
    context_object_name = 'forms'


class SubdivisionDetailDetailView(LoginRequiredMixin, DetailView):
    model = SubdivisionDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDetailCreateView(LoginRequiredMixin, CreateView):
    model = SubdivisionDetail
    form_class = SubdivisionDetailForm

    def form_valid(self, form):

        form.instance.subdivision_id = self.kwargs.get('pk')

        return super(SubdivisionDetailCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


class SubdivisionDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = SubdivisionDetail
    form_class = SubdivisionDetailForm

    # def form_valid( self, form ):
    #     #get the pk of the foreign key

    #     sd = SubdivisionDetail.objects.all()
    #     sd_filter = sd.filter(subdivision_id=self.object.subdivision.id)
    #     sum = sd_filter.aggregate(Sum('subtotal'))['subtotal__sum']
    #     # sum = Subdivision.objects.annotate(Sum('subdivisiondetail__subtotal'))

    #     s = Subdivision.objects.get(id=self.object.subdivision.id)
    #     s.total = sum

    #     s.save()
    #     # Subdivision.objects.filter(id = self.object.subdivision.id).update(total=sum)
    #     # form.instance.remarks =sum
    #     # form.save()
    #     return super(SubdivisionDetailUpdateView, self).form_valid(form)

    # def profile(request, self):
    #     if request.method == 'POST':
    #         form = SubdivisionForm(request.POST)

    #         if form.is_valid():

    #             sd = SubdivisionDetail.objects.all()
    #             sd_filter = sd.filter(subdivision_id=7)
    #             sum = sd_filter.aggregate(Sum('subtotal'))['subtotal__sum']
    #             # sum = Subdivision.objects.annotate(Sum('subdivisiondetail__subtotal'))

    #             form.instance.remarks =sum
    #             form.save()
    #             return redirect('form-list')

    # else:
    #   form = SubdivisionForm(request.POST, )

    # return render(request, 'members/register.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()

        return context


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'forms/upload.html', context)


def file_list(request, *args, **kwargs):
    files = Files.objects.all()
    forms = Forms.objects.all()
    subdivisiondetail = SubdivisionDetail.objects.all()
    
    context = {
        'files': files,
        'forms':forms,
        'subdivisiondetail':subdivisiondetail,
        'pk': kwargs.get('pk'),
        
        'object': kwargs.get('pk')
    }
    return render(request, 'forms/files_list.html', context)


def upload_file(request, *args, **kwargs):
    pk= kwargs.get('pk')
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('file_list', pk)
    else:
        form = FileForm()
    context = {
        'form': form, 
    }
    return render(request, 'forms/upload_file.html', context)


def delete_file(request, pk):
    if request.method == 'POST':
        files = Files.objects.get(pk=pk)
        files.delete()
    return redirect('home')


class FileListView(ListView):
    model = Files
    template_name = 'forms/class_file_list.html'
    context_object_name = 'files'


class UploadFileView(CreateView):
    model = Files
    form_class = FileForm
    success_url = reverse_lazy('class_file_list')
    template_name = 'forms/upload.html'
