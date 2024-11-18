# main.py
from fastapi import FastAPI, HTTPException # type: ignore
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from models import Brand
from typing import List

from datetime import datetime

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:3000",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://signa-frontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulación de una base de datos en memoria
brands = [
    Brand(
        id=1, 
        brand="Nike", 
        owner="Phil Knight", 
        status="active", 
        created_at=datetime(2023, 1, 1, 10, 0, 0), 
        updated_at=datetime(2023, 1, 1, 10, 0, 0),
    ),
    Brand(
        id=2, 
        brand="Adidas", 
        owner="Adolf Dassler", 
        status="active", 
        created_at=datetime(2023, 1, 2, 10, 0, 0), 
        updated_at=datetime(2023, 1, 2, 10, 0, 0),
    ),
    Brand(
        id=3, 
        brand="Puma", 
        owner="Rudolf Dassler", 
        status="active", 
        created_at=datetime(2023, 1, 3, 10, 0, 0), 
        updated_at=datetime(2023, 1, 3, 10, 0, 0),
    ),
    Brand(
        id=4, 
        brand="Under Armour", 
        owner="Kevin Plank", 
        status="inactive", 
        created_at=datetime(2023, 1, 4, 10, 0, 0), 
        updated_at=datetime(2023, 1, 4, 10, 0, 0),
    ),
    Brand(
        id=5, 
        brand="Reebok", 
        owner="Joe Foster", 
        status="active", 
        created_at=datetime(2023, 1, 5, 10, 0, 0), 
        updated_at=datetime(2023, 1, 5, 10, 0, 0),
    ),
    Brand(
        id=6, 
        brand="New Balance", 
        owner="Jim Davis", 
        status="active", 
        created_at=datetime(2023, 1, 6, 10, 0, 0), 
        updated_at=datetime(2023, 1, 6, 10, 0, 0),
    ),
    Brand(
        id=7, 
        brand="Asics", 
        owner="Kihachiro Onitsuka", 
        status="active", 
        created_at=datetime(2023, 1, 7, 10, 0, 0), 
        updated_at=datetime(2023, 1, 7, 10, 0, 0),
    ),
    Brand(
        id=8, 
        brand="Fila", 
        owner="Giansevero Fila", 
        status="inactive", 
        created_at=datetime(2023, 1, 8, 10, 0, 0), 
        updated_at=datetime(2023, 1, 8, 10, 0, 0),
    ),
    Brand(
        id=9, 
        brand="Converse", 
        owner="Marquis Mills Converse", 
        status="active", 
        created_at=datetime(2023, 1, 9, 10, 0, 0), 
        updated_at=datetime(2023, 1, 9, 10, 0, 0),
    ),
    Brand(
        id=10, 
        brand="Vans", 
        owner="Paul Van Doren", 
        status="inactive", 
        created_at=datetime(2023, 1, 10, 10, 0, 0), 
        updated_at=datetime(2023, 1, 10, 10, 0, 0),
    ),
]

@app.post("/brands/", response_model=Brand)
def create_brand(brand: Brand):
    brands.append(brand)
    return brand

@app.get("/brands/", response_model=List[Brand])
def list_brands():
    return brands

@app.get("/brands/{brand_id}", response_model=Brand)
def get_brand(brand_id: int):
    brand = next((m for m in brands if m.id == brand_id), None)
    if brand is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return brand

@app.put("/brands/{brand_id}", response_model=Brand)
def update_brand(brand_id: int, brand_updated: Brand):
    for i, m in enumerate(brands):
        if m.id == brand_id:
            brands[i] = brand_updated
            return brand_updated
    raise HTTPException(status_code=404, detail="Marca no encontrada")

@app.delete("/brands/{brand_id}")
def delete_brand(brand_id: int):
    global brands
    brands = [m for m in brands if m.id != brand_id]
    return {"detail": "Marca eliminada"}
