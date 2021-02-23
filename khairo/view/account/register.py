from fastapi.requests import Request
from fastapi import APIRouter, Form
from khairo.settings import template
from httpx import AsyncClient
from khairo.settings import  API_WEBSITE_URL,WEBSITE_URL
router = APIRouter()


@router.get("/register")
async def register(request: Request):
    return template('pages/register.html', {"request": request})

@router.post("/register")
async  def register(email:str = Form(...) , password:str = Form(...), confirmPassword:str= Form(...),
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
            return
    print(data.status_code)
