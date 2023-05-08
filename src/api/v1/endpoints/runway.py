from fastapi import APIRouter
from pentruBD.forConnection import airportBD as dbWorker
from model.modelRunway import runway

runway_router = APIRouter(prefix="/runway", tags=["runway"])
lucruBD=dbWorker()


@runway_router.get("/", tags=["runway"])
def get_runways():
    return lucruBD.get_runways()

@runway_router.get("/{runway_id}", tags=["runway"])
def get_runway_by_id(runway_id: int):
    return lucruBD.get_runway_by_id(runway_id)

@runway_router.put("/",tags=["runway"])
def put_runway(pista: runway):
    return lucruBD.put_runway(pista)

@runway_router.delete("/{runway_id}", tags=["runway"])
def del_runway_by_id(runway_id: int):
    return lucruBD.del_runway_by_id(runway_id)