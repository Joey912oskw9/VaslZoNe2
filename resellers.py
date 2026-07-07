# resellers.py
from fastapi import APIRouter

router = APIRouter()
token_router = APIRouter()

async def setup(config=None):
    pass

@router.get("/api/resellers")
async def list_resellers():
    return {"resellers": []}

@router.post("/api/resellers")
async def create_reseller():
    return {"ok": True}

@router.delete("/api/resellers/{id}")
async def delete_reseller(id: str):
    return {"ok": True}

@router.post("/api/resellers/{id}/reset-token")
async def reset_reseller_token(id: str):
    return {"ok": True}
