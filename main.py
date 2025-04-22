from fastapi import FastAPI

from models.storage_unit import StorageUnit

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/units")
def get_units():
    return {"data": "my self storage units"}

@app.post("/units")
def create_unit(payload:StorageUnit):
    print(payload)
    return {"new_unit": f"Created a new unit number {payload.unit_number} of size {payload.size}"}


## requirements for a new unit
## size, availability, price, unit_number, location