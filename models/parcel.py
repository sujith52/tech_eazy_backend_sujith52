# models/parcel.py

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.sqlite import TEXT
from database import Base

class Parcel(Base):
    __tablename__ = "parcels"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    delivery_address = Column(TEXT, nullable=False)
    contact_number = Column(String, nullable=False)
    parcel_size = Column(String, nullable=False)
    parcel_weight = Column(Float, nullable=False)
    tracking_id = Column(String, unique=True, index=True, nullable=False)
