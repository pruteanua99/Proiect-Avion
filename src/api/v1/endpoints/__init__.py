from fastapi import APIRouter
from .avion import items_router

api_endpoints = APIRouter()
api_endpoints.include_router(items_router)