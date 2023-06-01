from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListAPIView.as_view()),
    path('contact/', views.ContactListAPIView.as_view()),
    path('get-in-touch/', views.GetInTouchCreateAPIView.as_view())
]
