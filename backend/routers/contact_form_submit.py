from fastapi import APIRouter, Form, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import ContactFormModel
from db.database import get_db_session
from datetime import datetime, timedelta
from notifications.notify_tg_admins import send_telegram_notification

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
    
    # Check if last entry was made within 24 hours
    query = select(ContactFormModel).where(ContactFormModel.email == form_data.email).order_by(ContactFormModel.created_at.desc())
    result = await db.execute(query)
    existing_entry = result.scalars().first()
    if existing_entry and existing_entry.created_at > datetime.now() - timedelta(days=1):
        return JSONResponse(content={"message": "You have already submitted a form within the last 24 hours!"}, status_code=400)

    # Save the validated form data to the database
    contact_entry = ContactFormModel(name=form_data.name, email=form_data.email)
    db.add(contact_entry)
    await db.commit()
    await db.refresh(contact_entry)  # Ensure the object is fully loaded

    # Extract contact entry details
    contact_data = {
        "name": contact_entry.name,
        "email": contact_entry.email,
        "created_at": contact_entry.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }

    # Send notification to admins
    await send_telegram_notification(contact_data)

    # Process the validated form data
    return JSONResponse(
        content={"message": f"Hello, <b>{form_data.name}</b>! Form submitted successfully!"}, 
        status_code=200
    )
