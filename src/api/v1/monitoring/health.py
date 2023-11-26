from fastapi import APIRouter
from core.logger import logger

health_router = APIRouter()


@health_router.get("/")
async def health() -> dict:
    logger.debug("This is debug message")
    logger.info("This is info message")
    logger.warning("This is warning message")
    logger.error("This is error message")
    logger.critical("This is critical message")

    return {"status": "OK"}
