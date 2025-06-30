# schemas/parcel.py

from pydantic import BaseModel

class ParcelCreate(BaseModel):
    customer_name: str
    delivery_address: str
    contact_number: str
    parcel_size: str
    parcel_weight: float

class ParcelResponse(ParcelCreate):
    tracking_id: str

    class Config:
        orm_mode = True
