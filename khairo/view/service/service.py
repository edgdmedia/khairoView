from fastapi.requests import Request
from khairo.settings import template
from fastapi import Depends
from khairo.view.constant.accessViewMixin import ViewMixin
from khairo.view.generalView.index import main_router
from httpx import AsyncClient
from khairo.settings import API_WEBSITE_URL

@main_router.get('/service')
async def service(request: Request, user:dict = Depends(ViewMixin.get_user)):
    async with AsyncClient() as client:
        data = await client.get(f"{API_WEBSITE_URL}/service")
    if data.status_code == 200:
        return  template('pages/service/service.html', {'request': request, "user":user, "service":data.json()})
    return template('pages/service/service.html', {'request': request, "user": user})

