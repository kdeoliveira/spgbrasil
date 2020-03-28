from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('layout/', views.LayoutView.as_view(), name='layout'),
]