from httpx import AsyncClient
from khairo.settings import WEBSITE_URL
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi import status
import json
class ViewMixin(object):
    @staticmethod
    async  def get_user(request:Request):
        data = request.cookies.get("user")
        if data:
            user = json.loads(data)
            return user["user"]
        return RedirectResponse("/login", status_code=status.HTTP_302_FOUND)

    @staticmethod
    async  def get_user_details(request:Request):
        data = request.cookies.get("user")
        if data:
            user = json.loads(data)
            return user["user"]
        return None






