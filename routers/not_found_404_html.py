from fastapi import APIRouter
from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from config import PRODUCTION

router = APIRouter()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Define a custom 404 error handler
async def custom_404_handler(request: Request, exc: HTTPException):
    data = {
        "PRODUCTION": PRODUCTION,
        "title": "404 - Page Not Found | AAA Devs",
        "description": "The page you are looking for does not exist. Please check the URL and try again."
    }
    return templates.TemplateResponse("404.html", {"request": request, "data": data}, status_code=404)
