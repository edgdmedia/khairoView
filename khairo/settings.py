from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")
import os
template = Jinja2Templates(directory="./khairo/template").TemplateResponse
DEBUG = os.getenv("DEBUG")
WEBSITE_URL = os.getenv("WEBSITE_URL")
API_WEBSITE_URL = os.getenv("API_WEBSITE_URL")

