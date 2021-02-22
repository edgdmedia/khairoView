from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")


API_WEBSITE_URL =  "https://khairodiet.herokuapp.com/api/v1" #'http://127.0.0.1:8000/api/v1'
WEBSITE_URL = "https://khairodietview.herokuapp.com" #'http://127.0.0.1:3000'
DEBUG = False