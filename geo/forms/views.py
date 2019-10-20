from django import forms

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import SubdivisionForm, SubdivisionDetailForm, FormForm, FileForm, DivisionForm, CommentForm
from .models import Files

from django.forms.models import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Sum, Avg, F
from forms.models import Forms, SubdivisionDetail, Subdivision, Division, AccreditationType, Files, Comment
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
        context['files'] = Files.objects.all()
        context['year'] = 2019
        context['a'] = self.kwargs.get('pk')
        context['f'] = Forms.objects.all().order_by('-year')
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
        context['files'] = Files.objects.all()
        # files = Files.objects.exclude(note_from_auditor='')
        # count = files.count()
        
        # messages.add_message(self.request, messages.INFO, f'You have {count} note/s left')
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

            return redirect('form-list', self.kwargs.get('pk'))
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
    
    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse_lazy('form-list', kwargs={'pk': 1})

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

        # files = Files.objects.exclude(note_from_auditor='')
        # count = files.count()
        
        # messages.add_message(self.request, messages.INFO, f'You have {count} note/s left')

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

        # files = Files.objects.exclude(note_from_auditor='')
        # count = files.count()
        
        # messages.add_message(self.request, messages.INFO, f'You have {count} note/s left')

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

        # files = Files.objects.exclude(note_from_auditor='')
        # count = files.count()
        
        # messages.add_message(self.request, messages.INFO, f'You have {count} note/s left')

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

    def form_valid( self, form ):
        subpoints=form.cleaned_data['subpoints']
        subtotal=form.cleaned_data['subtotal']

        if subtotal > subpoints:
            form.instance.subtotal = subpoints
        #     return self.subpoints
        
        return super(SubdivisionDetailUpdateView, self).form_valid(form)

   

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


class FileListView(ListView):
    model = Files
    
    template_name = 'forms/files_list.html'

    

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        files = Files.objects.filter(pk=pk)
        
        comments = Comment.objects.filter(files=pk)
        comment2 = Comment.objects.all()
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.all()
        context['forms'] = Forms.objects.all()  
        context['subdivisiondetail'] =  SubdivisionDetail.objects.all()
        context['pk'] =  self.kwargs.get('pk')
        context['note'] = FileForm(),
        context['object'] =  self.kwargs.get('pk'),
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context


    
def upload_file(request, *args, **kwargs):
    pk= kwargs.get('pk')
    sd = SubdivisionDetail.objects.filter(pk=pk)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.instance.subdivisiondetail_id = pk

            form.save()
            
            return redirect('file_list', pk)
    else:
        form = FileForm()
        
    context = {
        'form': form, 
        'sd':sd
    }
    return render(request, 'forms/upload_file.html', context)

class FileDeleteView(DeleteView):
    model = Files
    fields = "__all__"
    template_name = 'forms/upload_file.html'
    def get_success_url( self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        id2 = self.kwargs.get('pk')
        
        return reverse_lazy('file_list', kwargs={'pk':self.object.subdivisiondetail.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.all()
        context['forms'] = Forms.objects.all()
        context['subdivisiondetail'] =  SubdivisionDetail.objects.all()
        context['pk'] =  self.kwargs.get('pk')
        context['note'] = FileForm,
        context['object'] =  self.kwargs.get('pk')

        return context





class FileUpdateView(UpdateView):
    model = Files
    form_class = FileForm
    
    template_name = 'forms/upload_file.html'

    def get_success_url( self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        id2 = self.kwargs.get('pk')
        
        return reverse_lazy('file_list', kwargs={'pk':self.object.subdivisiondetail.id})

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        files = Files.objects.filter(pk=pk)
        
        comments = Comment.objects.filter(files=pk).order_by('-pk')
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.all()
        context['forms'] = Forms.objects.all()
        context['subdivisiondetail'] =  SubdivisionDetail.objects.all()
        context['pk'] =  self.kwargs.get('pk')
        context['note'] = FileForm
        context['object'] =  self.kwargs.get('pk')
        context['comments'] = comments
        
        return context

class UploadFileView(CreateView):
    model = Files
    form_class = FileForm
    success_url = reverse_lazy('class_file_list')
    template_name = 'forms/upload.html'


class NoteUpdateView(UpdateView):
    model = Files 
    fields = 'note_from_auditor'
    context_object_name = 'n'
    


class CommentCreateView(CreateView):
    model= Comment
    form_class = CommentForm
    paginate_by = 5

    def form_valid( self, form, *args, **kwargs ):
        form.instance.files_id = self.kwargs.get('pk')
        form.instance.user = self.request.user
        return super(CommentCreateView, self).form_valid(form)
        
    
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        files = Files.objects.filter(pk=pk)
        
        comments = Comment.objects.filter(files=pk).order_by('-pk')
        paginated_comments = Paginator(comments, 3)
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.all()
        context['forms'] = Forms.objects.all()
        context['subdivisiondetail'] =  SubdivisionDetail.objects.all()
        context['pk'] =  self.kwargs.get('pk')
        context['note'] = FileForm
        context['object'] =  self.kwargs.get('pk')
        context['comments'] = comments
        
        return context

class CommentDeleteView(DeleteView):
    model = Comment

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        files = Files.objects.filter(pk=pk)
        
        comments = Comment.objects.filter(files=pk).order_by('-pk')
        paginated_comments = Paginator(comments, 3)
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.all()
        context['forms'] = Forms.objects.all()
        context['subdivisiondetail'] =  SubdivisionDetail.objects.all()
        context['pk'] =  self.kwargs.get('pk')
        context['note'] = FileForm
        context['object'] =  self.kwargs.get('pk')
        context['comments'] = comments
        context['f'] = Forms.objects.all()
        context['d'] = Division.objects.all()
        context['sd'] = Subdivision.objects.all()
        context['sdd'] = SubdivisionDetail.objects.all()
        return context
    
    def get_success_url(self, **kwargs):
        self.object = self.get_object()
        id1 = self.kwargs['pk']
        return reverse("comment-list", kwargs={"pk": self.object.files.pk})