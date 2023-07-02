from sqlalchemy.orm import Session

from . import models, schemas

def get_resolution(db: Session, resolution_id: int):
    return db.query(models.Resolution).filter(models.Resolution.id == resolution_id).first()

def get_resolutions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Resolution).offset(skip).limit(limit).all()

def create_resolution(db: Session, resolution: schemas.ResolutionCreate):
    db_resolution = models.Resolution(**resolution.dict())
    db.add(db_resolution)
    db.commit()
    db.refresh(db_resolution)
    return db_resolution

def get_suggestions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Suggestion).offset(skip).limit(limit).all()

def create_user_suggestion(db: Session, suggestion: schemas.SuggestionCreate, resolution_id: int):
    db_suggestion = models.Suggestion(**suggestion.dict(), resolution_id=resolution_id)
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

def update_resolution(db: Session, resolution: schemas.ResolutionUpdate):
    db_resolution = db.query(models.Resolution).filter(models.Resolution.id == resolution.id).first()
    if db_resolution is None:
        return None
    for var, value in vars(resolution).items():
        setattr(db_resolution, var, value) if value else None
    db.add(db_resolution)
    db.commit()
    db.refresh(db_resolution)
    return db_resolution
