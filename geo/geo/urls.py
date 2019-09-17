from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# from forms.views import upload, file_list, upload_file, delete_file, FileListView, UploadFileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    path('', include('dashboard.urls')),

    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='dashboard/password_reset.html'),
        name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='dashboard/password_reset_done.html'),
        name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='dashboard/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='dashboard/password_reset_complete.html'),
        name='password_reset_complete'),



    path('', include('forms.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
