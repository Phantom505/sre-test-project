from typing import Optional, Dict, Any
from pydantic import BaseModel

class ApiResponse(BaseModel):
    service_url: str
    response_code: int
    response_data: Dict[str, Any]
    created_at: str
