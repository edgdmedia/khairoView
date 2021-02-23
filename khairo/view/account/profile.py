from fastapi import APIRouter, Depends
from khairo.view.constant.accessViewMixin import ViewMixin
from fastapi.responses import RedirectResponse
from khairo.settings import template
from fastapi.requests import Request

router = APIRouter()

@router.get('/profile')
async def profile(request: Request, user:dict = Depends(ViewMixin.get_user)):
    if user:
        return template('pages/profile.html', {'request': request, "user":user})
    return RedirectResponse("/", status_code=302)