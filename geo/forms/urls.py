from django.urls import path, include
from .views import CoE_IT_FORM_FORMs
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('forms/', views.EditFormView, name='forms'),
    

]