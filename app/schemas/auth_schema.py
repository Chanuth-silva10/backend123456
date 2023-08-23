from uuid import UUID
from pydantic import BaseModel,EmailStr

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    user_id:UUID
    user:object
    
    
    
class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None