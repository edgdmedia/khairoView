from fastapi.requests import Request
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from fastapi import APIRouter, Form, status
from khairo.settings import template
from khairo.view.account.login import account_router
from httpx import AsyncClient
from typing import Optional
from khairo.settings import API_WEBSITE_URL, WEBSITE_URL
import  json


@account_router.get('/password/reset')
async def password_reset(request: Request):
    error = request.cookies.get("error", None)
    message = request.cookies.get("message", None)
    if error:
        return template('pages/account/change-password.html', {'request': request, "error":json.loads(error)})
    elif message:
        return template('pages/account/change-password.html', {'request': request, "message":json.loads(message)})
    return template('pages/account/change-password.html', {'request': request})

@account_router.post("/password/reset", response_class=RedirectResponse, )
async  def password_reset( response:Response, email:Optional[str] = Form(...)) -> RedirectResponse:

    if email:
        try:
            async  with AsyncClient() as client:
                data = await client.post(f"{API_WEBSITE_URL}/passwordResetting", json={"email": email,
                                     "passwordReset_url": f"{WEBSITE_URL}/password/change"})
            if data.status_code == 200:
                response = RedirectResponse('/password/reset', status_code=status.HTTP_302_FOUND)
                response.set_cookie(key="message", value=json.dumps({'message': 'A password reset link has been sent to your email'}), max_age=1)
                return response
            response = RedirectResponse('/password/reset', status_code=status.HTTP_302_FOUND)
            response.set_cookie(key="error", value=data.text , max_age=1)
            return response

        except:
            response = RedirectResponse('/password/reset', status_code=status.HTTP_302_FOUND)
            response.set_cookie(key="error", value=json.dumps({'error':'Error resetting password'}),max_age=1)
            return response
    response = RedirectResponse('/password/reset', status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="error", value=json.dumps({'error':'Your account email is required'}), max_age=1)
    return response




@account_router.get("/password/change/{userId}")
async def changePassword(request: Request, userId:str):
    error = request.cookies.get("error")
    if error:
       return template('pages/account/password-reset.html', {'request': request, "userId":userId, "error":json.loads(error)})
    return template('pages/account/password-reset.html', {'request': request, "userId": userId})


@account_router.post("/password/change")
async  def ChangePassword(password:Optional[str] = Form(...),
        confirmPassword:Optional[str] = Form(...), userId:Optional[str]= Form(...)) ->RedirectResponse:
    if password and confirmPassword and userId:
        try:
            async with AsyncClient() as client:
                data = await client.put(f"{API_WEBSITE_URL}/passwordReset", json={
                    "password": password,
                    "confirmPassword": confirmPassword,
                    "userId": userId
                })
            if data.status_code == 200:
                response = RedirectResponse("/login", status_code=status.HTTP_302_FOUND)
                response.set_cookie(key="message", value=json.dumps(data.json()[0]), max_age=1)
                return response
            response = RedirectResponse(f"/password/change/{userId}", status_code=302)
            response.set_cookie(key="error", value= json.dumps(data.json()), max_age=1 )
            return response
        except:
            response = RedirectResponse(f"/password/change/{userId}", status_code=302)
            response.set_cookie("error", value=json.dumps({'error':'error resetting password, try again'}), max_age=1)
            return response
    response = RedirectResponse(f"/password/change/{userId}", status_code=302)
    response.set_cookie("error", value=json.dumps({'error':'please provide your details'}), max_age=1)
    return response





