from django.shortcuts import render
from django.utils.translation import gettext
from .models import Page, Content
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title' : gettext('Homepage'),
        }
        return context



class LayoutView(TemplateView):
    template_name = "_base.html"
    base_file = "base"

    def get_context_data(self, **kwargs):
        try:
            page_model = Page.objects.get(name = self.base_file)
            content_model = Content.objects.filter(page_name = page_model)
        except:
            page_model=None
            content_model=None


        context = super().get_context_data(**kwargs)
        context = {
            'test' : 'teste',
            'page' : page_model,
            'content' : content_model,
        }
        return context


    # -- (DEV) LANG SESSIONS SETUP -- 
    # from django.utils import translation
    # user_language = 'pt_BR'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # -- Remove sessions' keys --
    # if translation.LANGAUGE_SESSION_KEY in request.session:
    #   del request.session[translation.LANGUAGE_SESSION_KEY]




