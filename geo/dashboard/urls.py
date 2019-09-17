from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),
    path('calendar/', views.calendar, name='calendar'),
    path('load-forms/', views.form_year, name='load-forms'),
    path('lockscreen/', views.lockscreen, name='lockscreen'),
    path('chairperson-forms/<int:pk>/',
         views.chairperson_forms, name='chairperson-forms'),
    path('', auth_views.LoginView.as_view(
        template_name='dashboard/login.html', redirect_authenticated_user=True), name='login'),
]
