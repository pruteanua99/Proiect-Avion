from fastapi import APIRouter, HTTPException
from model import Avion
from storage.dbWorker import dbWorker

items_router = APIRouter(prefix="/avion", tags=["avion"])
lucruBD=dbWorker()

@items_router.get("/", tags=['avion'])
def get_all_planes():
    return lucruBD.get_all_planes()

@items_router.get("/{avion_Id}", tags=['avion'])
def get_plane_by_NrId(avion_Id: int):
    avion_Id=int(avion_Id)
    return lucruBD.get_plane_by_NrId(avion_Id)

@items_router.put("/", tags=['avion'])
def put_plane(avion: Avion):
    return lucruBD.put_plane(avion)