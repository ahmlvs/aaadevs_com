from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, tags=["pages"])
async def index_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "AAA Devs"})
