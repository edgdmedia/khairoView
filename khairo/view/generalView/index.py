from fastapi.requests import Request
from fastapi import APIRouter, Depends
from khairo.settings import template
from khairo.view.constant.accessViewMixin import ViewMixin
main_router = APIRouter()


@main_router.get("/")
async def index(request: Request, user:dict = Depends(ViewMixin.get_user_details)):
    if user:
        return template("pages/base/base.html", {"request": request, "user": user})
    return template("pages/account/login.html", {"request": request, "user": user}, status_code=302)



@main_router.get('/settings')
async def settings(request: Request, user:dict = Depends(ViewMixin.get_user)):
    return template('pages/account/settings.html', {'request': request, "user":user})


@main_router.get('/help')
async def service(request: Request, user:dict = Depends(ViewMixin.get_user_details)):
    return template('pages/generalView/contact.html', {'request': request, "user":user})

@main_router.get("/404")
async def error_page(request:Request, user:dict = Depends(ViewMixin.get_user)):
    return template("pages/generalView/404.html", {"request": request, "user":user})
