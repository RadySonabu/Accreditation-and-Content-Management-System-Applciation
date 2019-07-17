from django.urls import path, include
from . import views
from .views import display_all_dean
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('download-excel/', views.export, name='download-excel'),
    path('deans/', views.display_all_dean, name='display_all_dean'),

]
