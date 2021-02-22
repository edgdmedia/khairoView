from pydantic import EmailStr, BaseModel
from khairo.view.model.customeFom import as_form

@as_form
class Login(BaseModel):
    email:EmailStr
    password:bytes