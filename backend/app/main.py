import os

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .api.v1.tournaments.exceptions import DomainException
from .api.v1.tournaments.router import router as tournament_router

cors_origins = os.getenv("CORS_ORIGINS", "").split(",")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}


app.include_router(router=tournament_router, prefix="/api/v1", tags=["tournaments"])


@app.exception_handler(DomainException)
async def handle_bad_request(_: Request, exc: DomainException):
    return JSONResponse(status_code=exc.get_status_code(), content={"detail": str(exc)})


@app.exception_handler(RequestValidationError)
async def handle_request_validation(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={"detail": exc.errors()},
    )
