from django.urls import resolve, reverse,path
from django.urls import register_converter
from django.utils import translation
from pages.urls import urlpatterns
from pages.models import Page
from www.locale import Locale
from django.conf import urls

class TranslationMiddleware:
    def __init__(self, arg):
        self.lang = 'en'
        self.get_response = arg
        self.locale = Locale()
        super().__init__()

    def __call__(self, request):

        # print("From session: "+translation.get_language_from_request(request))

        # if translation.LANGUAGE_SESSION_KEY in request.session:
        #     del request.session[translation.LANGUAGE_SESSION_KEY]
        
        # print(request.resolver_match.kwargs)
        # print(request.resolver_match)

        # print("From url: "+(request.path).split('/')[1])

        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


    def process_request(self, request):
        response = self.get_response(request)
        url = resolve(request.path)
        self.locale.start()
        # print("From process request: "+str(url.url_name))

        return response
    def process_response(self, request, response):
        print("End of request -> Response")

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("view process")
        return




