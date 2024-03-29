from django.shortcuts import render
from django.utils.translation import gettext as _, gettext_lazy
from .models import Page, Content
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import translation


sentence = 'teste de fdsfsdfsdf'
output = _(sentence)


class HomeView(TemplateView):
    template_name = "_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title' : _('Homepage'),
        }
        return context



class LayoutView(TemplateView):
    base_url = None
    template_name = 'pages/single_context.html'
    
    def get_context_data(self, *args, **kwargs):
        try:
            page_model = Page.objects.get(name = self.base_url)
            content_model = Content.objects.filter(page_name = page_model)
        except:
            page_model=None
            content_model=None

        context = super(LayoutView, self).get_context_data(*args,**kwargs)

        context.update({
            'page' : page_model,
            'content' : list(content_model),        
            })
        return context
    
        # def get(self, request, *args, **kwargs):
        #     kevin = _("kevin de oliveira")
        #     data = self.get_context_data(*args,**kwargs)
        #     data.update({'kev':kevin})
        #     return render(request,self.template_name, data)


        # -- (DEV) LANG SESSIONS SETUP -- 
        # from django.utils import translation
        # user_language = 'pt_BR'
        # translation.activate(user_language)
        # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        # -- Remove sessions' keys --
        # if translation.LANGAUGE_SESSION_KEY in request.session:
        #   del request.session[translation.LANGUAGE_SESSION_KEY]


class PageList(ListView):
    base_url = None
    template_name = 'pages/page_list.html'
    model= Page

    # objct_list #
    def get_context_data(self, *args, **kwargs):
        try:
            page_model = Page.objects.get(name = self.base_url)
            content_model = Content.objects.filter(page_name = page_model)
        except:
            page_model=None
            content_model=None
        
        context = super(PageList, self).get_context_data(*args,**kwargs)

        context.update({
            'page' : page_model,
            'content' : list(content_model),        
            })
        return context

class PageDetail(DetailView):
    base_url = ''
    template_name_field = ['pages/simple_d.html','pages/complex_d.html',]

    slug_url_kwarg = 'url_page'
    slug_field = 'name'

    url_templates ={
        'sectors': ['industry', 'industria', 'marine', 'infrastructure'],
        'expertise': ['coating', 'pavement', 'handling'],
    }

    def dispatch(self, request, *args, **kwargs):
        # if translation.LANGUAGE_SESSION_KEY in request.session:
        #     del request.session[translation.LANGUAGE_SESSION_KEY]
        url_value = (request.path).strip('/').split('/')
        print(url_value)
        self.base_url = url_value[-1]
        try:
            self.queryset = Page.objects.filter(lang = translation.get_language())
        except Exception:
            print("page does not have langauge "+(request.path).split('/')[1])
            request.status_code = 404

        dispatch_value = super(PageDetail, self).dispatch(request,*args,**kwargs)
        
        return dispatch_value




    def get_template_names(self):
        if self.base_url in self.url_templates['sectors']:
            return self.template_name_field[0]
        elif self.base_url in self.url_templates['expertise']:
            return self.template_name_field[1]

        # object_list #
    def get_context_data(self, *args, **kwargs):
        try:
            print(self.base_url)
            page_model = Page.objects.get(name = self.base_url)
            content_model = Content.objects.filter(page_name = page_model)
            print(content_model)
        except:
            page_model=None
            content_model=None

        context = super(PageDetail, self).get_context_data(*args,**kwargs)

        context.update({
            'page' : page_model,
            'content' : list(content_model),
            })
        return context
