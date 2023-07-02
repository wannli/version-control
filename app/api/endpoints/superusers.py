```python
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/superuser/resolution/", response_model=schemas.Resolution)
def create_resolution(resolution: schemas.ResolutionCreate, db: Session = Depends(get_db)):
    db_resolution = crud.get_resolution_by_text(db, text=resolution.text)
    if db_resolution:
        raise HTTPException(status_code=400, detail="Resolution already exists")
    return crud.create_resolution(db=db, resolution=resolution)

@router.get("/superuser/resolution/", response_model=List[schemas.Resolution])
def read_resolutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resolutions = crud.get_resolutions(db, skip=skip, limit=limit)
    return resolutions

@router.put("/superuser/resolution/{resolution_id}", response_model=schemas.Resolution)
def update_resolution(resolution_id: int, resolution: schemas.ResolutionCreate, db: Session = Depends(get_db)):
    db_resolution = crud.get_resolution(db, resolution_id=resolution_id)
    if not db_resolution:
        raise HTTPException(status_code=404, detail="Resolution not found")
    return crud.update_resolution(db=db, resolution=resolution, resolution_id=resolution_id)

@router.post("/superuser/suggestion/{suggestion_id}/accept", response_model=schemas.Suggestion)
def accept_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    db_suggestion = crud.get_suggestion(db, suggestion_id=suggestion_id)
    if not db_suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return crud.accept_suggestion(db=db, suggestion_id=suggestion_id)

@router.post("/superuser/suggestion/{suggestion_id}/reject", response_model=schemas.Suggestion)
def reject_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    db_suggestion = crud.get_suggestion(db, suggestion_id=suggestion_id)
    if not db_suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return crud.reject_suggestion(db=db, suggestion_id=suggestion_id)
```