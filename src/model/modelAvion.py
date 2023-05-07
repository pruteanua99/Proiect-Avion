from pydantic import BaseModel
from typing import Optional
from datetime import date,time


class Avion(BaseModel):


    avion_id: Optional[int]
    nrIdentificare: str
    model: str

    
    # sursa: str
    # destinatia: str
    # tip_zbor: str
    # motiv: str
    # pista: int 
    # poarta: int
    # dataAterizare: Optional[date]
    # dataPlecare: Optional[date]
    # oraPlecare: Optional[time]
    # oraAterizare: Optional[time]

if  __name__ == "__main__":
    avion = Avion(avion_id=1,nrIdentificare="alex",model="alex")