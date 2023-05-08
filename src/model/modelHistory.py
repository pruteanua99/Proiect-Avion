from pydantic import BaseModel
from typing import Optional
from datetime import date,time


class History(BaseModel):

    Istoric_Id:Optional[int]
    Avion_Id: str
    tipZbor: Optional[str]
    sursa: Optional[str]
    destinatia: Optional[str]
    motiv: Optional[str]
    dataAterizare: Optional[date]
    dataPlecare: Optional[date]
    poarta: Optional[int]
    pistaFolosita: Optional[int]
    oraPlecare: Optional[time]
    oraAterizare: Optional[time]

