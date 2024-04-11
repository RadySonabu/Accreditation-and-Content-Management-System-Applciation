from django.urls import path
from .views import job
urlpatterns = [
    path('job/', job, name="job-job")
]
