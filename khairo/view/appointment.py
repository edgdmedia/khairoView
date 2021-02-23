from fastapi.requests import Request
from khairo.settings import template
from fastapi import APIRouter

router = APIRouter()
@router.get('/appointment')
async def appointment(request: Request):
    return template('pages/appointment.html', {'request': request})
