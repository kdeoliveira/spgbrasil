from . import views
from django.urls import path
from django.utils.translation import gettext_lazy

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('layout/', views.LayoutView.as_view(base_url = 'base', template_name = "_base.html"), name='layout'),
    path(gettext_lazy('sectors/'), views.LayoutView.as_view(base_url = 'sectors', template_name = "_base.html"), name='sectors'),
    path(gettext_lazy('group/'), views.LayoutView.as_view(base_url = 'group', template_name = "_base.html"), name='group'),

]