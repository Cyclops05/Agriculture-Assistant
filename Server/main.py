from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example data model for a crop query
class CropQuery(BaseModel):
    crop_name: str
    location: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Agriculture Assistant API"}

# Example POST endpoint for crop advice
@app.post("/crop-advice")
def get_crop_advice(query: CropQuery):
    # Placeholder logic — replace with real ML model or database lookup
    if query.crop_name.lower() == "wheat":
        return {
            "crop": query.crop_name,
            "location": query.location,
            "advice": "Wheat grows best in cool, dry climates. Consider sowing in November."
        }
    else:
        return {
            "crop": query.crop_name,
            "location": query.location,
            "advice": "No specific advice available yet. Please check back soon."
        }