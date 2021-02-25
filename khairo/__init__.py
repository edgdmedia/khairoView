from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from khairo.view.generalView import index
from khairo.view.service import service
from khairo.view import appointment, plan
from khairo.view.account import  login, register, profile, passwordManager
from khairo.settings import template

app = FastAPI(debug=True)
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/404", status_code=302)

app.mount("/static", StaticFiles(directory="./khairo/static"), name="static")
app.include_router(login.account_router, tags=["khairo/router/Account"])
app.include_router(index.main_router, tags=["khairo/router"])



