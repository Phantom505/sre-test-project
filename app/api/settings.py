from fastapi import APIRouter
from app.models import ChangeResponseFormat
from app.core.config import settings
import json
import logging

router = APIRouter()


@router.post("/settings/changeResponseFormat/", response_model=ChangeResponseFormat)
async def change_response_format(new_settings: ChangeResponseFormat):
    settings.response_format = new_settings.format
    settings.include_metadata = new_settings.metadata
    settings.response_application = new_settings.application

    settings.save_to_file('config.json')

    response_data = {
        "format": settings.response_format,
        "metadata": settings.include_metadata,
        "application": settings.response_application
    }

    logging.info(f"Updated settings: {response_data}")
    return response_data
