# SPDX-License-Identifier: GPL-3.0
# QuartNG
# A textboard with the kitchen sink included
#
# main.py
#
# COPYRIGHT NOTICE
# Copyright (C) 2025 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

# SPDX-License-Identifier: GPL-3.0
# QuartNG - main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from lib.core import globals as GLOBAL
from lib.core.page import returnPage
from lib.core import logger as QuartNG_logger

import logging
import os
import jinja2
import importlib
import uvicorn

def initialize():
    if not os.path.exists("data"):
        os.makedirs("data")
        GLOBAL.INIT = True

def load_plugins(app: FastAPI):
    for plugin in GLOBAL.PLUGINS:
        try:
            module = importlib.import_module(plugin)
            if hasattr(module, 'router'):
                app.include_router(module.router)
                QuartNG_logger.log("main", f"Plugin {plugin} loaded with {len(module.router.routes)} pages.")
            else:
                QuartNG_logger.log_warning("main", f"Plugin {plugin} has no router.")
        except ImportError as e:
            QuartNG_logger.log_error("main", f"Failed to load plugin {plugin}: {e}")

def create_app() -> FastAPI:
    app = FastAPI(
        title=GLOBAL.NAME,
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )

    @app.middleware("http")
    async def log_request_info(request: Request, call_next):
        response = await call_next(request)

        status = response.status_code
        msg = f"{request.method} {request.url} - {status}"

        if status == 200:
            QuartNG_logger.log("main", f"Request: {msg}")
        elif status == 500:
            QuartNG_logger.log_error("main", f"INTERNAL SERVER ERROR: {msg}")
            return returnPageHTML(
                request=request,
                main_content="QuartNG had an internal error. Please try again later or report this error.",
                footer_content="Error code: 500",
                status_code=500
            )
        else:
            QuartNG_logger.log_warning("main", f"Request: {msg}")
        return response

    return app

def silence_uvicorn_logs():
    logging.getLogger("uvicorn").setLevel(logging.CRITICAL)

if __name__ == "__main__":
    silence_uvicorn_logs()
    initialize()

    app = create_app()
    load_plugins(app)
    GLOBAL.INIT = False
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")
