```python
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Suggestion)
def create_suggestion(
    *, db: Session = Depends(get_db), suggestion_in: schemas.SuggestionCreate
):
    suggestion = crud.suggestion.create(db=db, obj_in=suggestion_in)
    return suggestion


@router.get("/", response_model=List[schemas.Suggestion])
def read_suggestions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suggestions = crud.suggestion.get_multi(db, skip=skip, limit=limit)
    return suggestions


@router.get("/{id}", response_model=schemas.Suggestion)
def read_suggestion(*, db: Session = Depends(get_db), id: int):
    suggestion = crud.suggestion.get(db=db, id=id)
    if not suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return suggestion


@router.put("/{id}", response_model=schemas.Suggestion)
def update_suggestion(
    *,
    db: Session = Depends(get_db),
    id: int,
    suggestion_in: schemas.SuggestionUpdate,
):
    suggestion = crud.suggestion.get(db=db, id=id)
    if not suggestion:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    suggestion = crud.suggestion.update(db=db, db_obj=suggestion, obj_in=suggestion_in)
    return suggestion
```