from abc import ABC, abstractmethod
from typing import List
from model import modelAvion as Avion
from porti.Aeroport import locParcare
import pymysql
import datetime


class StorageObject(ABC):
    
    # @abstractmethod
    # def get_gate_by_Id(self, gate_id: int) -> locParcare:
    #     raise NotImplementedError("Functia get_gate_by_Id neimplementata")
    
    
    @abstractmethod
    def get_all_planes(self) -> List[object]:
        raise NotImplementedError("Functie get_all_planes neimplementata")
    
    @abstractmethod
    def get_plane_by_NrId(self, avion_Id: int) -> List[object]:
        raise NotImplementedError ("Functia get_plane_by_id neimplementata")
    
    @abstractmethod
    def put_plane(self, object: object) -> bool:
        raise NotImplementedError("Functia add_plane neimplementata")
    
    # @abstractmethod
    # def get_runway_by_id(self, runway_id: int) -> int:
    #     raise NotImplementedError("Functia get_runway_by_id neimplementata")
    
    # @abstractmethod
    # def get_history_by_NrId(self , nrIdentificare: str) -> dict:
    #     raise NotImplementedError("Fuctia get_history_by_NrId neimplementata")
    
    # @abstractmethod
    # def get_history_by_Date  (self, data: datetime) -> dict:
    #     raise ("Functia get_history_by_date neimplementata")
    
    # @abstractmethod
    # def del_plane_by_NrId(self, avion_Id: int) -> bool:
    #     raise ("Functia del_plane_by_NrId neimplementata")
    
    # @abstractmethod
    # def has_plane_by_NrId(self, avion_Id: int) -> bool:
    #     raise ("Functia has_plane_by_NrId neimplementata")
    
    # @abstractmethod
    # def set_plane_by_NrId(self, plane: Avion) -> bool:
    #     raise ("Functia has_plane_by_NrId neimplementata")

class Singleton(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance