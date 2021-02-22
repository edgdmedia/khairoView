from fastapi.requests import Request
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from fastapi import APIRouter, Form, status
from khairo import template
from khairo.settings import API_WEBSITE_URL
from typing import Optional
import json



router = APIRouter()
from httpx import AsyncClient


@router.get("/login")
async def login(request: Request):
    error = request.cookies.get("error")
    message = request.cookies.get("message")
    if error:
        return template('pages/login.html', {"request": request, "error":json.loads(error)})
    elif message:
        return template('pages/login.html', {"request": request, "message": json.loads(message)})
    return template('pages/login.html', {"request": request})


@router.get("/logout")
async  def Logout(response:Response)->RedirectResponse:
    response  = RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("user")
    return response




@router.post("/login")
async def login(response: Response, request:Request, email: Optional[str] = Form(...),
                password: Optional[str] = Form(...))->RedirectResponse:
    if email and password:
        try:
            async  with AsyncClient() as client:
                data = await client.post(url=f'{API_WEBSITE_URL}/login',
                                         json={"email": email, "password": password})
                if data.status_code == 200:
                    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
                    response.set_cookie("user", value=json.dumps(data.json()), httponly=True)
                    return response
                else:
                    return template("pages/login.html", {"request": request, "error": json.dumps(data.json())})
        except:
            return template("pages/login.html",
                            {"request": request, 'error': json.dumps({'message': 'authorization failed, try again'})})
    response.set_cookie(key="error", value=json.dumps({'message':'Invalid details provided'}), expires=300)
    return RedirectResponse("/login", status_code=status.HTTP_302_FOUND)



