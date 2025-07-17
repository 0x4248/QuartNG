from fastapi import FastAPI, Request, Header, HTTPException, UploadFile, File, Form, Response, APIRouter
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse, FileResponse


from fastapi import Request
from lib.core.page import returnPage
import lib.core.globals as GLOBAL
from lib.plugins import components as c

from lib.core import settings
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return returnPage(
        request=request,
        top_components=[c.style.center_text([
                c.b.h(1, f"Welcome to {GLOBAL.NAME}"),
                c.util.Time.current(self_update=True),
                c.s.Link.text_decor("/posts", "Example"),
                " ",
                c.s.Link.text_decor("/login", "Login")
            ]),
            c.b.hr()
        ],
        main_components=[
            c.s.half_split(
                left=[
                    c.b.h(2, "What is QuartNG?"),
                    c.lorem.lorem_ipsum_p(4)
                ],
                right=[
                    c.b.h(2, "What can I do with it?"),
                    c.lorem.lorem_ipsum_p(4)
                ]
            )
        ]
    )
