from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    cif: str
    name: str
    surname: str
    number: str
    email: str
    created_at: datetime

class ChangeResponseFormat(BaseModel):
    format: Optional[str] = "default"
    metadata: Optional[bool] = False
    application: Optional[str] = "json"
