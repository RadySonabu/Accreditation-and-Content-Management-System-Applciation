from django.urls import path, include
from .views import CreateForm_FORMs, EditFormView
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('create_form/', views.EditFormView, name='create_form'),
    
    ]