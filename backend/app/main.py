from fastapi import FastAPI, HTTPException

from .schemas import (
    UserOut,
    UserCreate,
    UserUpdate,
    DomainOut
)

from .services import profile, domain

app = FastAPI(title="Career Intelligence Platform")

# ---------- Startup ----------
@app.on_event("startup")
async def startup_event():
    await profile.init_db()
    await domain.seed_domains()

# ---------- Profile APIs ----------
@app.post("/profile/", response_model=UserOut)
async def create_user_endpoint(user: UserCreate):
    return await profile.create_user(user)

@app.get("/profile/{user_id}", response_model=UserOut)
async def get_user_endpoint(user_id: int):
    user = await profile.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/profile/{user_id}", response_model=UserOut)
async def update_user_endpoint(user_id: int, user: UserUpdate):
    updated_user = await profile.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/profile/{user_id}", response_model=UserOut)
async def delete_user_endpoint(user_id: int):
    deleted_user = await profile.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

# ---------- Domain APIs ----------
@app.get("/domains/", response_model=list[DomainOut])
async def list_domains():
    return await domain.get_all_domains()
