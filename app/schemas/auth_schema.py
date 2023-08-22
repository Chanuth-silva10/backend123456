from uuid import UUID
from pydantic import BaseModel,EmailStr

class TokenSchema(BaseModel):
    user:object
    
    
class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None