from fastapi import APIRouter
from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from config import PROFILES

router = APIRouter()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Define a custom 404 error handler
async def custom_404_handler(request: Request, exc: HTTPException):
    data = {
        "PROFILES": PROFILES,
        "page": "404",
        "title": "404 - Page Not Found | AAA Devs",
        "description": "The page you are looking for does not exist. Please check the URL and try again.",
        "url": "https://aaadevs.com/404",
        "canonical": "https://aaadevs.com/404",
        "image": "/static/images/capibara.webp",
        "robots": "noindex, nofollow",
    }
    return templates.TemplateResponse(request, "404.html", {"request": request, "data": data}, status_code=404)
