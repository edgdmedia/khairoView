from fastapi.requests import Request
from khairo.settings import template
from khairo.view.constant.accessViewMixin import ViewMixin
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

router = APIRouter()
@router.get('/appointment')
async def appointment(request: Request, user:dict = Depends(ViewMixin.get_user)):
    if user:
        return template('pages/appointment.html', {'request': request, "user":user})
    return RedirectResponse("/", status_code=302)
