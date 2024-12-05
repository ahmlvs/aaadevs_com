from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import index_html, contact_form_submit, not_found_404_html
from db.database import async_engine
from db.models import Base
import uvicorn


app = FastAPI()

# Mount a static folder (if needed for CSS/JS files)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the routers
app.include_router(index_html.router)
app.include_router(contact_form_submit.router, prefix="/api/v1")

# Register the global 404 handler
app.add_exception_handler(404, not_found_404_html.custom_404_handler)

# Define startup function
async def startup_event():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Register the startup event handler
app.add_event_handler("startup", startup_event)


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    PRODUCTION = os.getenv("PRODUCTION", "False") == "True"

    if PRODUCTION:
        uvicorn.run("main:app", host="127.0.0.1", port=8000)
    else:
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
