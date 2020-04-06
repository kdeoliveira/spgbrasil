from . import views
from django.urls import path
from django.utils.translation import gettext_lazy

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('layout/', views.LayoutView.as_view(base_url = 'base', template_name = "_base.html"), name='layout'),

    path(gettext_lazy('sectors/'), views.PageList.as_view(base_url = 'sectors'), name='sectors'),
    path(gettext_lazy('sectors/<slug:url_page>'), views.PageDetail.as_view(), name='sector_details'),

    path(gettext_lazy('expertise/'), views.PageList.as_view(base_url = 'expertise'), name='expertise'),
    path(gettext_lazy('expertise/<slug:url_page>'), views.PageDetail.as_view(), name='expertise_details'),

    path(gettext_lazy('green'), views.LayoutView.as_view(base_url = 'green'), name='green'),

    path(gettext_lazy('group/'), views.LayoutView.as_view(base_url = 'group'), name='group'),
]