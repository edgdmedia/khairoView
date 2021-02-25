from fastapi import APIRouter, Depends
from khairo.view.constant.accessViewMixin import ViewMixin
from fastapi.responses import RedirectResponse
from khairo.settings import template
from fastapi.requests import Request
from khairo.view.account.login import account_router

@account_router.get('/profile')
async def profile(request: Request, user:dict = Depends(ViewMixin.get_user)):
    if user:
        if user["active"]:
            return template('pages/account/admin/admin_profile.html',{'request': request, "user":user})
        elif user["dietitian"]:
            return template('pages/account/admin/dietitian_profile.html',{'request': request, "user":user})
        return template('pages/account/profile.html', {'request': request, "user":user})
    return RedirectResponse("/", status_code=302)