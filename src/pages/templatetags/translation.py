from django import template
from html.parser import HTMLParser

#STATIC METHODS AND CLASSES

# class HTMLTags(HTMLParser):
#     def __init__(self):
#         self.reset()
#         self.strict = False
#         self.convert_charrefs = True
#         self.fed = []
#     def handle_data(self, arg):
#         self.fed.append(arg)
#     def get_data(self):
#         return ''.join(self.fed)

# def strip_tags(html):
#     string = HTMLTags()
#     string.feed(html)
#     return string.get_data()

# TAG TEMPLATE

# LIST SPLIT BY ;

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