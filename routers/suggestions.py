```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db
from ..middleware.authentication import get_current_user

router = APIRouter()

@router.post("/suggestions/", response_model=schemas.Suggestion)
def create_suggestion(suggestion: schemas.SuggestionCreate, db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    db_suggestion = models.Suggestion(**suggestion.dict(), user_id=user.id)
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

@router.get("/suggestions/", response_model=List[schemas.Suggestion])
def get_suggestions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suggestions = db.query(models.Suggestion).offset(skip).limit(limit).all()
    return suggestions

@router.get("/suggestions/{suggestion_id}", response_model=schemas.Suggestion)
def get_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    suggestion = db.query(models.Suggestion).filter(models.Suggestion.id == suggestion_id).first()
    if suggestion is None:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return suggestion

@router.delete("/suggestions/{suggestion_id}")
def delete_suggestion(suggestion_id: int, db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    suggestion = db.query(models.Suggestion).filter(models.Suggestion.id == suggestion_id).first()
    if not suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    if suggestion.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db.delete(suggestion)
    db.commit()
    return {"detail": "Suggestion deleted"}

@router.put("/suggestions/{suggestion_id}", response_model=schemas.Suggestion)
def update_suggestion(suggestion_id: int, suggestion: schemas.SuggestionCreate, db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    db_suggestion = db.query(models.Suggestion).filter(models.Suggestion.id == suggestion_id).first()
    if not db_suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    if db_suggestion.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    for key, value in suggestion.dict().items():
        setattr(db_suggestion, key, value)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion
```