from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from backend.app.api.v1.tournaments.application.exceptions import ApplicationException
from backend.app.api.v1.tournaments.domain.exceptions import DomainException
from backend.app.api.v1.tournaments.router import router as tournament_router

app = FastAPI()


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}


app.include_router(router=tournament_router, prefix="/api/v1", tags=["tournaments"])


@app.exception_handler(DomainException)
async def handle_bad_request(_: Request, exc: DomainException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exc)}
    )


@app.exception_handler(ApplicationException)
async def handle_not_found(_: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=status.HTTP_404_BAD_REQUEST, content={"detail": str(exc)}
    )


@app.exception_handler(RequestValidationError)
async def handle_request_validation(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={"detail": exc.errors()},
    )
