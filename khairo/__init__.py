from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.templating import Jinja2Templates
from khairo.view import appointment, index, plan, service
from khairo.view.account import login, register, passwordManager, profile

app = FastAPI(debug=True)
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")

app.mount("/static", StaticFiles(directory="./khairo/static"), name="static")
template = Jinja2Templates(directory="./khairo/template").TemplateResponse
app.include_router(index.router)
app.include_router(plan.router)
app.include_router(appointment.router)
app.include_router(service.router)
app.include_router(login.router)
app.include_router(register.router)
app.include_router(passwordManager.router)
app.include_router(profile.router)

