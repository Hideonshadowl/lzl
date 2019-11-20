from django.contrib import admin
from django.urls import path
from login import views
urlpatterns = [
    path(r'login/', views.LoginView.as_view()),
    path(r'rellogin/', views.RelLoginView.as_view()),
    path(r'blog/', views.BlogView.as_view()),
    path(r'blog2/', views.BlogView2.as_view()),
]