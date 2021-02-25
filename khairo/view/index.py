from fastapi.requests import Request
from fastapi import APIRouter, Depends
from khairo.settings import template
from khairo.view.constant.accessViewMixin import ViewMixin
router = APIRouter()


@router.get("/")
async def index(request: Request, user:dict = Depends(ViewMixin.get_user_details)):
    if user:
        return template("base.html", {"request": request, "user": user})
    return template("pages/login.html", {"request": request, "user": user}, status_code=302)



@router.get('/settings')
async def settings(request: Request, user:dict = Depends(ViewMixin.get_user)):
    return template('pages/settings.html', {'request': request, "user":user})


@router.get('/help')
async def service(request: Request, user:dict = Depends(ViewMixin.get_user_details)):
    return template('pages/contact.html', {'request': request, "user":user})

@router.get("/404")
async def errorpage(request:Request, user:dict = Depends(ViewMixin.get_user)):
    return template("404.html", {"request": request, "user":user})
