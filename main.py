```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models
from routers import users, superusers, resolutions, suggestions

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(superusers.router)
app.include_router(resolutions.router)
app.include_router(suggestions.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```