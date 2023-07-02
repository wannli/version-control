```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db
from ..middleware.authorization import verify_superuser

router = APIRouter()

@router.post("/resolutions/", response_model=schemas.Resolution)
def create_resolution(resolution: schemas.ResolutionCreate, db: Session = Depends(get_db), current_superuser: models.SuperUser = Depends(verify_superuser)):
    db_resolution = models.Resolution(text=resolution.text, superuser_id=current_superuser.id)
    db.add(db_resolution)
    db.commit()
    db.refresh(db_resolution)
    return db_resolution

@router.get("/resolutions/", response_model=List[schemas.Resolution])
def get_resolutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resolutions = db.query(models.Resolution).offset(skip).limit(limit).all()
    return resolutions

@router.get("/resolutions/{resolution_id}", response_model=schemas.Resolution)
def get_resolution(resolution_id: int, db: Session = Depends(get_db)):
    db_resolution = db.query(models.Resolution).filter(models.Resolution.id == resolution_id).first()
    if db_resolution is None:
        raise HTTPException(status_code=404, detail="Resolution not found")
    return db_resolution

@router.delete("/resolutions/{resolution_id}")
def delete_resolution(resolution_id: int, db: Session = Depends(get_db), current_superuser: models.SuperUser = Depends(verify_superuser)):
    db_resolution = db.query(models.Resolution).filter(models.Resolution.id == resolution_id).first()
    if db_resolution is None:
        raise HTTPException(status_code=404, detail="Resolution not found")
    db.delete(db_resolution)
    db.commit()
    return {"detail": "Resolution deleted"}

@router.put("/resolutions/{resolution_id}", response_model=schemas.Resolution)
def update_resolution(resolution_id: int, resolution: schemas.ResolutionCreate, db: Session = Depends(get_db), current_superuser: models.SuperUser = Depends(verify_superuser)):
    db_resolution = db.query(models.Resolution).filter(models.Resolution.id == resolution_id).first()
    if db_resolution is None:
        raise HTTPException(status_code=404, detail="Resolution not found")
    db_resolution.text = resolution.text
    db.commit()
    db.refresh(db_resolution)
    return db_resolution
```