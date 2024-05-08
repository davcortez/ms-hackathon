import typing as t
from fastapi import Depends, HTTPException, status
from internal.config import get_settings
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer


settings = get_settings()
get_bearer_token = HTTPBearer(auto_error=False)


def get_token(
    auth: t.Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
):
    """Check if api key is valid"""
    if auth is None or (token := auth.credentials) not in settings.api_keys:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Forbidden")
    return token
