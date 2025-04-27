from fastapi import APIRouter, HTTPException, Response, Header
from app.models import User
from app.core.config import settings
from app.core.logging_config import setup_logging
from datetime import datetime, timezone
import json
import logging

timestamp = datetime.now(timezone.utc).isoformat()
created_at = datetime.now(timezone.utc).isoformat()

router = APIRouter()

setup_logging()

# Sample user data
users = [
    {"id": 1, "cif": "6525359", "name": "Knaz", "surname": "Aftandil", "number": "1234567890",
     "email": "knaz@example.com", "created_at": "2022-08-19"},
    {"id": 2, "cif": "6852021", "name": "Zulfiyye", "surname": "Xanlar", "number": "2345678901", "email": "zulfiyye@example.com",
     "created_at": "2024-08-18"},
    {"id": 3, "cif": "3658962", "name": "Elnur", "surname": "Gambar", "number": "3456789012",
     "email": "elnur@example.com", "created_at": "2024-04-15"},
    {"id": 4, "cif": "8525365", "name": "Saida", "surname": "Yusubova", "number": "4567890123",
     "email": "saida@example.com", "created_at": "2023-07-21"},
    {"id": 5, "cif": "9652324", "name": "Kamran", "surname": "Muslumov", "number": "5678901234", "email": "kamran@example.com",
     "created_at": "2021-08-10"},
]

def log_request(service_url: str, response_code: int, response_data: dict):
    log_entry = {
        "service_url": service_url,
        "response_code": response_code,
        "response_data": response_data,
        "created_at": created_at
    }
    logging.info(json.dumps(log_entry))

@router.get("/users/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    accept: str = Header(None, description="Specify the response format using Accept header: 'application/json' or 'application/xml'")
):
    user_data = next((u for u in users if u["id"] == user_id), None)
    if not user_data:
        log_request(f"/api/v1/users/{user_id}", 404, {"detail": "User not found"})
        raise HTTPException(status_code=404, detail="User not found")

    # Convert to User model to ensure proper format
    user = User(**user_data)

    response_data = user.dict()

    if settings.response_format == "detailed":
        response_data["details"] = {"createdAt": user.created_at.isoformat()}

    if settings.include_metadata:
        response_data["metadata"] = {
            "status": "success",
            "timestamp": timestamp
        }

    # Determine response format based on Accept header
    if accept == "application/xml":
        try:
            import dicttoxml
            xml_data = dicttoxml.dicttoxml(response_data)
            return Response(content=xml_data, media_type="application/xml")
        except ImportError:
            raise HTTPException(status_code=500, detail="XML formatting library not installed")
    else:
        # Fallback to JSON format
        return response_data
