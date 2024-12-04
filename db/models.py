from sqlalchemy import Column, Integer, String
from db.database import Base

class ContactFormDB(Base):
    __tablename__ = "contact_form"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
