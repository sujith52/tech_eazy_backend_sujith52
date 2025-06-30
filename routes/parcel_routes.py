# routes/parcel_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.parcel import ParcelCreate, ParcelResponse
from services.parcel_service import (
    create_parcel,
    get_all_parcels,
    get_parcel_by_tracking_id
)
from database import get_db
from typing import List

router = APIRouter()

# Create a parcel
@router.post("/", response_model=ParcelResponse)
def create_new_parcel(parcel: ParcelCreate, db: Session = Depends(get_db)):
    return create_parcel(db, parcel)

# Get all parcels
@router.get("/", response_model=List[ParcelResponse])
def fetch_all_parcels(db: Session = Depends(get_db)):
    return get_all_parcels(db)

# Get parcel by tracking ID
@router.get("/{tracking_id}", response_model=ParcelResponse)
def fetch_parcel_by_tracking_id(tracking_id: str, db: Session = Depends(get_db)):
    parcel = get_parcel_by_tracking_id(db, tracking_id)
    if not parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return parcel
