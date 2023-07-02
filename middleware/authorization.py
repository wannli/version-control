from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from .authentication import get_current_superuser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def verify_superuser(token: str = Depends(oauth2_scheme), current_superuser: str = Depends(get_current_superuser)):
    if not current_superuser:
        raise HTTPException(
            status_code=403,
            detail="Not a superuser",
        )
    return current_superuser