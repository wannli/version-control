```python
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    suggestions = relationship("Suggestion", back_populates="user")

class SuperUser(Base):
    __tablename__ = "superusers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    resolutions = relationship("Resolution", back_populates="superuser")

class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    superuser_id = Column(Integer, ForeignKey("superusers.id"))
    superuser = relationship("SuperUser", back_populates="resolutions")
    suggestions = relationship("Suggestion", back_populates="resolution")

class Suggestion(Base):
    __tablename__ = "suggestions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="suggestions")
    resolution_id = Column(Integer, ForeignKey("resolutions.id"))
    resolution = relationship("Resolution", back_populates="suggestions")
```