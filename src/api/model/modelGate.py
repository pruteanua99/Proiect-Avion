from pydantic import BaseModel
from typing import Optional
class Gate(BaseModel):

    Poarta_fel: str
    Poarta_Referinta:Optional[int] 