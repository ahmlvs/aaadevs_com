from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import PRODUCTION

router = APIRouter()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@router.get("/animation", response_class=HTMLResponse, tags=["pages"])
async def index_html(request: Request):
    data = {
        "PRODUCTION": PRODUCTION,
        "page": "animation",
        "title": "",
        "description": "",
        "url": "",
        "canonical": "",
        "image": "",
        "robots": "noindex, nofollow",
    }
    return templates.TemplateResponse("animation.html", {"request": request, "data": data})
