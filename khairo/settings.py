from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")
import os
template = Jinja2Templates(directory="./khairo/template").TemplateResponse
DEBUG = os.getenv("DEBUG")

# WEBSITE_URL = "https://khairodietview.herokuapp.com"
# API_WEBSITE_URL =   "https://khairodiet.herokuapp.com/api/v1"
WEBSITE_URL = 'http://127.0.0.1:3000'
API_WEBSITE_URL =   'http://127.0.0.1:8000/api/v1'

