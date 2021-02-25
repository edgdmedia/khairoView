from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi import Depends
from khairo.view.generalView.index import main_router
from khairo.view.constant.accessViewMixin import ViewMixin
from khairo.settings import template



@main_router.get('/plan')
async def plan(request: Request, user:dict = Depends(ViewMixin.get_user) ):
    if user:
        return template('pages/plan/plan.html', {'request': request, "user":user})
    return RedirectResponse("/", status_code=302)
