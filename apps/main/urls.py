from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.CatalogListAPIView.as_view()),
    path('catalog-video/', views.CatalogVideoListAPIView.as_view()),
    path('property/', views.PropertyListAPIView.as_view()),
    path('property/<int:pk>/', views.PropertyRetrieveAPIView.as_view()),
]
