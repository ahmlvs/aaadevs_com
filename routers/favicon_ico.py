from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

# Route to serve the robots.txt file
@router.get("/favicon.ico", response_class=FileResponse, include_in_schema=False)
async def get_favicon_ico():
    return FileResponse("favicon.ico", media_type="image/x-icon", status_code=200)
