from model.modelGate import Gate
from pentruBD.forConnection import airportBD as dbWorker
from fastapi import APIRouter

gate_router = APIRouter(prefix="/gate" , tags=["gate"])
lucruDB = dbWorker()

@gate_router.get("/",tags=["gate"])
def get_gates():
    return lucruDB.get_gates()

@gate_router.get("/{gate_id}", tags=["gate"])
def get_gate_by_id(gate_id: int):
    return lucruDB.get_gate_by_Id(gate_id)

@gate_router.put("/", tags=["gate"])
def put_gate(poarta: Gate):
    return lucruDB.put_gate(poarta)

@gate_router.delete("/{gate_id}",tags=["gate"])
def del_gate(gate_id: int):
    return lucruDB.del_gate(gate_id)

@gate_router.post("/{gate_id}", tags=["gate"])
def update_gate(gate_id: int, poarta: Gate):
    return lucruDB.update_gate(gate_id,poarta)

