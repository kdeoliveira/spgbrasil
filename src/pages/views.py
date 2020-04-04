from django.shortcuts import render
from django.utils.translation import gettext as _, gettext_lazy
from .models import Page, Content
from django.views.generic.base import TemplateView
from django.template.loader import render_to_string

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
    
    def get_context_data(self, *args, **kwargs):

        try:
            page_model = Page.objects.get(name = self.base_url)
            content_model = Content.objects.filter(page_name = page_model)
        except:
            page_model=None
            content_model=None

        context = super(LayoutView, self).get_context_data(*args,**kwargs)

            # cnt = []
            # for x in list(content_model):
            #     cnt.append(_(x.content_text))
            #     cnt.append(_('%(main)s' % {'main':x.content_text,}))


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