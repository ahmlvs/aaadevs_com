from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

# Route to serve the robots.txt file
@router.get("/robots.txt", response_class=FileResponse, tags=["files"])
async def get_robots_txt():
    return FileResponse("robots.txt", media_type="text/plain", status_code=200)
