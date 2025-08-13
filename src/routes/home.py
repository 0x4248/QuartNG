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
        top_components=[
            c.base.h(1, "Hello Ella"),
            c.base.hr(),
        ],
        main_components=[
            c.base.h(2, "This is a test"),
            c.lorem.lorem_ipsum_p(4)
        ],
        bottom_components=[
            c.base.hr(),
            c.base.p("This is the bottom text", class_name="hello")  
        ]
    )
