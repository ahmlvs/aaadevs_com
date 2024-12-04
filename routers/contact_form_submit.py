from fastapi import APIRouter
from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.orm import Session
from db.models import ContactFormDB
from db.get_db import get_db

router = APIRouter()

# Define a Pydantic model for form validation
class ContactForm(BaseModel):
    name: str
    email: EmailStr

@router.post("/contact_form_submit", response_class=JSONResponse, tags=["api"])
async def contact_form_submit(
    name: str = Form(...), 
    email: str = Form(...),
    db: Session = Depends(get_db),
):
    # Validate form data using Pydantic
    try:
        form_data = ContactForm(name=name, email=email)
    except ValidationError as e:
        # return JSONResponse(content={"message": f"Form validation failed: {e.errors()}"}, status_code=400)
        return JSONResponse(content={"message": "Incorrect form data!"}, status_code=400)
    
    # Save the validated form data to the database
    contact_entry = ContactFormDB(name=form_data.name, email=form_data.email)
    db.add(contact_entry)
    db.commit()

    # Process the validated form data
    return JSONResponse(content={"message": f"Form submitted successfully! Hello, {form_data.name}!"}, status_code=200)
