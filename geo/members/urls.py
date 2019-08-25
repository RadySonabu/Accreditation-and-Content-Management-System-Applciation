from django.urls import path, include
from . import views
from .views import load_college, load_program
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user-list', views.UserListView.as_view(), name='user_changelist'),
    path('add/', views.UserCreateView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('<int:pk>/', views.UserUpdateView.as_view(), name='user_change'),
    path('download-excel/', views.export, name='download-excel'),
    path('ajax/load-college/', views.load_college, name='ajax_load_college'),
    path('ajax/load-program/', views.load_program, name='ajax_load_program')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
