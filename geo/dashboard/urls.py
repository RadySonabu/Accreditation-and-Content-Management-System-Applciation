from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),
    path('lockscreen/', views.lockscreen, name='lockscreen'),
    
]
