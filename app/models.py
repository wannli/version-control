```python
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    is_superuser = Column(Boolean, default=False)
    suggestions = relationship("Suggestion", back_populates="user")

class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    version = Column(Integer, nullable=False)
    suggestions = relationship("Suggestion", back_populates="resolution")

class Suggestion(Base):
    __tablename__ = "suggestions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    resolution_id = Column(Integer, ForeignKey("resolutions.id"))
    user = relationship("User", back_populates="suggestions")
    resolution = relationship("Resolution", back_populates="suggestions")
```