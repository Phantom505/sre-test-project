from fastapi import HTTPException
from fastapi.responses import JSONResponse

def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc.detail), "status_code": exc.status_code}
    )
