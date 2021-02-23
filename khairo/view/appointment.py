from fastapi.requests import Request
from khairo.settings import template
from khairo.view.constant.accessViewMixin import ViewMixin
from fastapi import APIRouter, Depends

router = APIRouter()
@router.get('/appointment')
async def appointment(request: Request, user:dict = Depends(ViewMixin.get_user)):
    return template('pages/appointment.html', {'request': request, "user":user["user"]})
