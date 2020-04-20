from django import template
from django.urls import resolve, reverse
from django.utils.translation import activate, get_language,check_for_language, LANGUAGE_SESSION_KEY, gettext_lazy, gettext

register = template.Library()
@register.filter
def translation(value, arg):
    output = ''
    if arg == "<p>":
        output = "<p> %s </p>" % (value)
    elif arg == "<span>":
        output = "<span> %s </span>" % (value)

    elif arg == "<li>":
        li = str(value).strip().split(';')
        for x in li:
            output += "<li> %s </li>" % (x)

    elif arg == "<object>":
        output = "<object> %s </object>" % (value)

    elif arg == "<div>":
        output = "<div> %s </div>" % (value)
    else:
        output = "<div> %s </div>" % (value)
    return output.strip()

@register.filter
def slug_trans(val):
    rt = gettext(val)
    return "%s" % (rt)

@register.simple_tag(takes_context=True, name="change_lang")
# Template executed when rendering template and after lang choosen and new rendering executed
# One skipped for disabled language link
def change_lang(context, lang=None, *args, **kwargs):
    req = context['request']
    path = req.path
    url_parts = resolve(path)
    url = path
    cur_lang = get_language()
    try:
        #Prepare href links
        activate(lang)  
        url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
    finally:
        if check_for_language(lang):
            activate(cur_lang)
            req.session[LANGUAGE_SESSION_KEY] = cur_lang
    return url