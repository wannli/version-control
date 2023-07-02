```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db
from ..middleware.authentication import get_current_superuser

router = APIRouter()

@router.post("/superusers/", response_model=schemas.SuperUser)
def create_superuser(superuser: schemas.SuperUserCreate, db: Session = Depends(get_db)):
    db_superuser = models.SuperUser(email=superuser.email)
    db.add(db_superuser)
    db.commit()
    db.refresh(db_superuser)
    return db_superuser

@router.get("/superusers/", response_model=List[schemas.SuperUser])
def get_superusers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    superusers = db.query(models.SuperUser).offset(skip).limit(limit).all()
    return superusers

@router.get("/superusers/{superuser_id}", response_model=schemas.SuperUser)
def get_superuser(superuser_id: int, db: Session = Depends(get_db)):
    db_superuser = db.query(models.SuperUser).filter(models.SuperUser.id == superuser_id).first()
    if db_superuser is None:
        raise HTTPException(status_code=404, detail="Superuser not found")
    return db_superuser

@router.delete("/superusers/{superuser_id}")
def delete_superuser(superuser_id: int, db: Session = Depends(get_db)):
    db.query(models.SuperUser).filter(models.SuperUser.id == superuser_id).delete()
    db.commit()
    return {"detail": "Superuser deleted"}

@router.put("/superusers/{superuser_id}", response_model=schemas.SuperUser)
def update_superuser(superuser_id: int, superuser: schemas.SuperUserCreate, db: Session = Depends(get_db)):
    db_superuser = db.query(models.SuperUser).filter(models.SuperUser.id == superuser_id).first()
    if db_superuser is None:
        raise HTTPException(status_code=404, detail="Superuser not found")
    for key, value in superuser.dict().items():
        setattr(db_superuser, key, value)
    db.commit()
    db.refresh(db_superuser)
    return db_superuser
```