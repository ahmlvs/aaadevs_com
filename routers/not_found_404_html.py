from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Define a custom 404 error handler
async def custom_404_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request, "title": "404 - Page Not Found | AAA Devs"}, status_code=404)
