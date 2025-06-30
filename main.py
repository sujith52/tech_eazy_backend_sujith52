# main.py

from fastapi import FastAPI
from database import engine, Base
from routes.parcel_routes import router as parcel_router

# Create the app
app = FastAPI(title="Zero Mile Delivery System")

# Create tables from models
Base.metadata.create_all(bind=engine)

# Include parcel routes
app.include_router(parcel_router, prefix="/parcels", tags=["Parcels"])
