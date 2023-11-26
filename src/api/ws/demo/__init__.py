from fastapi import APIRouter

from .test import health_router_ws

monitoring_router_ws = APIRouter()
monitoring_router_ws.include_router(
    health_router_ws,
)

__all__ = ["monitoring_router_ws"]
