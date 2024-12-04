from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import index_html, contact_form_submit
from db.database import engine
from db.models import Base
import uvicorn

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount a static folder (if needed for CSS/JS files)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the routers
app.include_router(index_html.router)
app.include_router(contact_form_submit.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
