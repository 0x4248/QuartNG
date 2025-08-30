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
            c.base.h(1, "PAGE: DEMO"),
            c.base.hr(),
        ],
        main_components=[
            c.base.h(2, "SYSTEM DEMO"),
        ],
        bottom_components=
                c.style.stick([
                    c.base.hr(),
                    c.btn_grids.row_container_center([
                        "<button>FN1</button>",
                        "<button>FN2</button>",
                        "<button>FN3</button>",
                        "<button>FN4</button>",
                        "<button>FN5</button>",
                        "<button>HOME</button>",
                        "<button style='color: red;'>DEL</button>",
                        "<button>BACK</button>",
                        "<button>↑</button>",
                        "<button>FWD</button>",
                        "<button>FLAG</button>",
                        "<button>CLEAR</button>",
                        "<button>←</button>",
                        "<button>↓</button>",
                        "<button>→</button>",
                ])
            ])
        )
