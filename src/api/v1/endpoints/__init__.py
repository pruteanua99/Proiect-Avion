from fastapi import APIRouter
from .avion import plane_router
from.runway import runway_router
from .gate import gate_router
from .history import history_router

api_endpoints = APIRouter()

api_endpoints.include_router(plane_router)
api_endpoints.include_router(runway_router)
api_endpoints.include_router(gate_router)
api_endpoints.include_router(history_router)