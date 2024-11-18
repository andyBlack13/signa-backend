# models.py
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Brand(BaseModel):
    id: Optional[int]
    brand: str
    owner: str
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
