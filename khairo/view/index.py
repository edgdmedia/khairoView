from fastapi.requests import Request
from fastapi import APIRouter, Depends
from khairo.settings import template
from khairo.view.constant.accessViewMixin import ViewMixin
router = APIRouter()


@router.get("/")
async def index(request: Request, user:dict = Depends(ViewMixin.get_user_details)):
    return template("base.html", {"request": request, "user": user})

@router.get('/service')
async def service(request: Request, user:dict = Depends(ViewMixin.get_user_details)):
    return template('pages/service.html', {'request': request, "user":user})


@router.get('/settings')
async def settings(request: Request, user:dict = Depends(ViewMixin.get_user)):
    return template('pages/settings.html', {'request': request, "user":user})


@router.get('/help')
async def service(request: Request, user:dict = Depends(ViewMixin.get_user_details)):
    return template('pages/contact.html', {'request': request, "user":user})
