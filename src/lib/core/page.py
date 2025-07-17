
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from datetime import datetime
from lib.core.responses import String
from lib.core.globals import JNINJA_ENV

from lib.core import globals as GLOBAL
import markdown

def compile(components: list) -> str:
    """
    Compiles a list of components and string elements into a single HTML string.
    """
    ret = ""
    for component in components:
        if callable(component):
            ret += component()
        else:
            ret += str(component)
    return ret

def returnPage(request: Request,
                top_components: list = [],
                main_components: list = [],
                bottom_components: list = [],
                title: str = GLOBAL.NAME,
                description: str = GLOBAL.DESCRIPTION,
                status_code: int = 200,
                css: str = None) -> HTMLResponse:

    with open("src/lib/static/css/base.css", "r") as f:
        css = f.read()

    top = compile(top_components)
    main = compile(main_components)
    bottom = compile(bottom_components) 
    
    template = JNINJA_ENV.get_template("base.html")
    return HTMLResponse(template.render(
        title=title,
        description=description,
        top=top,
        main=main,
        bottom=bottom,
        css=css
    ),
        status_code=status_code,
    )

