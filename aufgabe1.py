import html

def createHtmlBlockElement(type, classname=None, id=None, style=None, content=None, text=None):
    _classname = ""
    _id =""
    _style = ""
    _content = ""
    if not (classname == None):
        _classname = 'class="{0}" '.format(classname)
    if not (id == None):
        _id = 'id="{0}" '.format(id)
    if not (style == None):
        _style = 'style="{0}" '.format(style)
    if not (content == None):
        _content = content
    elif not (text == None):
        _content = html.escape(text)
    
    return "<{0} {1} {2} {3}>{4}</{0}>".format(type,_classname,_id,_style,_content)

print(createHtmlBlockElement("span", text="Webung <:)"))