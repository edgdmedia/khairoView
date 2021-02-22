from fastapi import APIRouter, Depends
from khairo.view.constant.accessViewMixin import ViewMixin
from khairo  import template
from fastapi.requests import Request

router = APIRouter()

@router.get('/profile')
async def profile(request: Request, user:dict = Depends(ViewMixin.get_user)):
    return template('pages/profile.html', {'request': request, "user":user})