from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

# Route to serve the robots.txt file
@router.get("/sitemap.xml", response_class=FileResponse)
async def get_sitemap_xml():
    return FileResponse("sitemap.xml", media_type="text/xml", status_code=200)
