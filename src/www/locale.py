from django.utils import translation
from django.conf import settings



url = ['admin/','administrador/']

class Locale:
    def __init__(self):
        self.cur_lang = None
        self.val = None
        self.available_lang = settings.LANGUAGES

    def start(self):
        self.val = translation.get_language()

    def trans(self):
        self.cur_lang = translation.get_language()
        print("available: "+str(self.available_lang))
        return "administradora/"

def get_trans():
    ll = Locale()
    return ll.trans()