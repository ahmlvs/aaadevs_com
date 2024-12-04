from fastapi import APIRouter, Form, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import ContactFormModel
from db.database import get_db_session

router = APIRouter()

# Define a Pydantic model for form validation
class ContactFormSchema(BaseModel):
    name: str
    email: EmailStr

@router.post("/contact_form_submit", response_class=JSONResponse, tags=["api"])
async def contact_form_submit(
    name: str = Form(...), 
    email: str = Form(...),
    db: AsyncSession = Depends(get_db_session),
):
    # Validate form data using Pydantic
    try:
        form_data = ContactFormSchema(name=name, email=email)
    except ValidationError as e:
        # return JSONResponse(content={"message": f"Form validation failed: {e.errors()}"}, status_code=400)
        return JSONResponse(content={"message": "Incorrect form data!"}, status_code=400)
    
    # Check for duplicate email (optional)
    query = select(ContactFormModel).where(ContactFormModel.email == form_data.email)
    result = await db.execute(query)
    existing_entry = result.scalars().first()
    if existing_entry:
        return JSONResponse(content={"message": "Email already exists!"}, status_code=400)

    # Save the validated form data to the database
    contact_entry = ContactFormModel(name=form_data.name, email=form_data.email)
    db.add(contact_entry)
    await db.commit()

    # Process the validated form data
    return JSONResponse(
        content={"message": f"Form submitted successfully! Hello, {form_data.name}!"}, 
        status_code=200
    )
