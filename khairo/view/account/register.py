from fastapi.requests import Request
from fastapi import APIRouter, Form
from khairo.settings import template
from fastapi.responses import RedirectResponse, Response
from httpx import AsyncClient
from khairo.settings import  API_WEBSITE_URL,WEBSITE_URL
import json
router = APIRouter()



@router.get("/register")
async def register(request: Request):
    error = request.cookies.get("error")
    if error:
        return template('pages/register.html', {"request": request, "error":json.loads(error)})
    return template('pages/register.html', {"request": request})

@router.post("/register")
async  def register(response:Response, email:str = Form(...) , password:str = Form(...), confirmPassword:str= Form(...),
                    gender:str= Form(...), phoneNo:str= Form(...),
                    firstname:str= Form(...), lastname:str= Form(...)):
    async with AsyncClient() as client:
        data = await client.post(f"{API_WEBSITE_URL}/register", json={
            "firstname":firstname,
            "lastname":lastname,
            "email": email,
            "phoneNo":phoneNo,
            "gender":gender,
            "confirmPassword":confirmPassword,
            "password":password,
            "email_verify_url":WEBSITE_URL
        })
        if data.status_code == 201:
            response = RedirectResponse("/login", status_code=302)
            response.set_cookie(key="message", value=data.text, max_age=1)
            return response
        response =  RedirectResponse("/register", status_code=302)
        response.set_cookie(key="error", value=data.text, max_age=1)
        return response

@router.get("/{userId}/verify")
async def verify_email(userId:str, response:Response):
     async with AsyncClient() as client:
         data = await client.post(f"{API_WEBSITE_URL}/user/{userId}/activate")
         if data.status_code == 200:
             response = RedirectResponse("/login", status_code=302)
             response.set_cookie(key="message", value=data.text, max_age=1)
             return response
         response = RedirectResponse("/login", status_code=302)
         response.set_cookie(key="error", value=data.text, max_age=1)
         return response





