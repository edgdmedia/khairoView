from fastapi.requests import Request
from khairo.settings import template
from fastapi import APIRouter,Depends
from khairo.view.constant.accessViewMixin import ViewMixin
router = APIRouter()

@router.get('/service')
async def service(request: Request, user:dict = Depends(ViewMixin.get_user)):
    return template('pages/service.html', {'request': request, "user":user["user"]})
