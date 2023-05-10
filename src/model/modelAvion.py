from pydantic import BaseModel
from typing import Optional


class Avion(BaseModel):


    avion_id: Optional[int]
    nrIdentificare: str
    model: str


if  __name__ == "__main__":
    avion = Avion(avion_id=1,nrIdentificare="alex",model="alex")