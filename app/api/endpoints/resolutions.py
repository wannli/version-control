from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/resolutions/", response_model=schemas.Resolution)
def create_resolution(resolution: schemas.ResolutionCreate, db: Session = Depends(get_db)):
    db_resolution = crud.get_resolution_by_text(db, text=resolution.text)
    if db_resolution:
        raise HTTPException(status_code=400, detail="Resolution already exists")
    return crud.create_resolution(db=db, resolution=resolution)

@router.get("/resolutions/", response_model=schemas.Resolution)
def read_resolutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resolutions = crud.get_resolutions(db, skip=skip, limit=limit)
    return resolutions

@router.get("/resolutions/{resolution_id}", response_model=schemas.Resolution)
def read_resolution(resolution_id: int, db: Session = Depends(get_db)):
    db_resolution = crud.get_resolution(db, resolution_id=resolution_id)
    if db_resolution is None:
        raise HTTPException(status_code=404, detail="Resolution not found")
    return db_resolution

@router.put("/resolutions/{resolution_id}", response_model=schemas.Resolution)
def update_resolution(resolution_id: int, resolution: schemas.ResolutionCreate, db: Session = Depends(get_db)):
    db_resolution = crud.get_resolution(db, resolution_id=resolution_id)
    if db_resolution is None:
        raise HTTPException(status_code=404, detail="Resolution not found")
    return crud.update_resolution(db=db, resolution=resolution, resolution_id=resolution_id)