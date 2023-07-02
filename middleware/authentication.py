```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from schemas import User, SuperUser
from models import User as UserModel, SuperUser as SuperUserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    user = db.query(UserModel).filter(UserModel.token == token).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return User.from_orm(user)

def get_current_superuser(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> SuperUser:
    superuser = db.query(SuperUserModel).filter(SuperUserModel.token == token).first()
    if not superuser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return SuperUser.from_orm(superuser)
```