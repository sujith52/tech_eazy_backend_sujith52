# services/parcel_service.py

from sqlalchemy.orm import Session
from models.parcel import Parcel
from schemas.parcel import ParcelCreate
import uuid

# Generate unique tracking ID
def generate_tracking_id():
    return str(uuid.uuid4())[:8]  # Short unique ID

# Create a new parcel
def create_parcel(db: Session, parcel_data: ParcelCreate):
    tracking_id = generate_tracking_id()
    db_parcel = Parcel(**parcel_data.dict(), tracking_id=tracking_id)
    db.add(db_parcel)
    db.commit()
    db.refresh(db_parcel)
    return db_parcel

# Get all parcels
def get_all_parcels(db: Session):
    return db.query(Parcel).all()

# Get parcel by tracking ID
def get_parcel_by_tracking_id(db: Session, tracking_id: str):
    return db.query(Parcel).filter(Parcel.tracking_id == tracking_id).first()
