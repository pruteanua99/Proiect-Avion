from model.modelHistory import History
from pentruBD.forConnection import airportBD as dbWorker
from fastapi import APIRouter

history_router=APIRouter(prefix="/history", tags=["history"])
lucruBD = dbWorker()

@history_router.get("/{Avion_Id}",tags=["history"])
def get_history_by_NrId(Avion_Id: str):
    return lucruBD.get_history_by_NrId(Avion_Id)