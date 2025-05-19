from pydantic import BaseModel

class StorageUnit(BaseModel):
    size: str
    available: bool
    price: float
    unit_number: int
    location: str
    id: str
    created_at: str