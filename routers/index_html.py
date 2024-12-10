from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import PRODUCTION

router = APIRouter()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, tags=["pages"])
async def index_html(request: Request):
    data = {
        "PRODUCTION": PRODUCTION,
        "page": "index",
        "title": "AAA Devs - Building Telegram and Discord Apps to Scale Your Business",
        "description": "AAA Devs creates innovative Telegram and Discord applications designed to help your business build, scale, and thrive.",
        "url": "https://aaadevs.com",
        "canonical": "https://aaadevs.com",
        "image": "/static/images/logo.webp",
        "robots": "index, follow",
    }
    return templates.TemplateResponse("index2.html", {"request": request, "data": data})
