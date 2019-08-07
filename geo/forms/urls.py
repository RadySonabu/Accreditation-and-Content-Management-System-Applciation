from django.urls import path, include
from . import views
from .views import (FormListView, FormDetailView,
                    FormCreateView, FormUpdateView,
                    FormDeleteView, DivisionCreateView,
                    DivisionListView, DivisionDetailView,
                    DivisionUpdateView, DivisionDeleteView,
                    SubdivisionListView, SubdivisionDetailView,
                    SubdivisionUpdateView, SubdivisionDeleteView,
                    SubdivisionCreateView, SubdivisionDetailListView,
                    SubdivisionDetailView,
                    SubdivisionDetailUpdateView, SubdivisionDetailDeleteView,
                    SubdivisionDetailCreateView
                    )
urlpatterns = [
    path('form/', FormListView.as_view(), name='form-list'),
    path('form/<int:pk>/', FormDetailView.as_view(), name='form-detail'),
    path('form/<int:pk>/update', FormUpdateView.as_view(), name='form-update'),
    path('form/<int:pk>/delete', FormDeleteView.as_view(), name='form-delete'),
    path('form/new/', FormCreateView.as_view(), name='form-create'),
    # ----------------------------------------------------------------------------------
    path('division/', DivisionListView.as_view(), name='division-list'),
    path('division/<int:pk>/', DivisionDetailView.as_view(), name='division-detail'),
    path('division/<int:pk>/update',
         DivisionUpdateView.as_view(), name='division-update'),
    path('division/<int:pk>/delete',
         DivisionDeleteView.as_view(), name='division-delete'),
    path('division/new/', DivisionCreateView.as_view(), name='division-create'),
    # ----------------------------------------------------------------------------------
    path('subdivision/', SubdivisionListView.as_view(), name='subdivision-list'),
    path('subdivision/<int:pk>/',
         SubdivisionDetailView.as_view(), name='subdivision-detail'),
    path('subdivision/<int:pk>/update',
         SubdivisionUpdateView.as_view(), name='subdivision-update'),
    path('subdivision/<int:pk>/delete',
         SubdivisionDeleteView.as_view(), name='subdivision-delete'),
    path('subdivision/new/', SubdivisionCreateView.as_view(),
         name='subdivision-create'),
    # ----------------------------------------------------------------------------------
    path('subdivision-detail/', SubdivisionDetailListView.as_view(),
         name='subdivision-detail-list'),
    path('subdivision-detail/<int:pk>/',
         SubdivisionDetailView.as_view(), name='subdivision-detail-detail'),
    path('subdivision-detail/<int:pk>/update',
         SubdivisionDetailUpdateView.as_view(), name='subdivision-detail-update'),
    path('subdivision-detail/<int:pk>/delete',
         SubdivisionDetailDeleteView.as_view(), name='subdivision-detail-delete'),
    path('subdivision-detail/new/', SubdivisionDetailCreateView.as_view(),
         name='subdivision-detail-create'),

]
