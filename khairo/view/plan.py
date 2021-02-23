from fastapi.requests import Request
from fastapi import APIRouter, Depends
from khairo.view.constant.accessViewMixin import ViewMixin
from khairo.settings import template
router = APIRouter()


@router.get('/plan')
async def plan(request: Request, user:dict = Depends(ViewMixin.get_user) ):
    return template('pages/plan.html', {'request': request, "user":user["user"]})
