from fastapi import APIRouter
from model import Avion
from pentruBD.forConnection import airportBD as dbWorker

plane_router = APIRouter(prefix="/avion", tags=["avion"])
lucruBD=dbWorker()

@plane_router.get("/", tags=['avion'])
def get_all_planes():
    return lucruBD.get_all_planes()

@plane_router.get("/{avion_Id}", tags=['avion'])
def get_plane_by_NrId(avion_Id: int):
    avion_Id=int(avion_Id)
    return lucruBD.get_plane_by_NrId(avion_Id)

@plane_router.put("/", tags=['avion'])
def put_plane(avion: Avion):
    return lucruBD.put_plane(avion)