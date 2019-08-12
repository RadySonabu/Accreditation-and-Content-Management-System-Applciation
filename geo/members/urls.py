from django.urls import path, include
from . import views
from .views import load_college, load_program
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.UserListView.as_view(), name='user_changelist'),
    path('add/', views.UserCreateView.as_view(), name='register'),
    path('<int:pk>/', views.UserUpdateView.as_view(), name='user_change'),
    path('download-excel/', views.export, name='download-excel'),
    path('ajax/load-college/', views.load_college, name='ajax_load_college'),
    path('ajax/load-program/', views.load_program, name='ajax_load_program')
]
