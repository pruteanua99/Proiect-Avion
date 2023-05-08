from abc import ABC, abstractmethod
from typing import List


class StorageObject(ABC):
    
    @abstractmethod
    def get_gate_by_Id(self, gate_id: int) -> List[object]:
        raise NotImplementedError("Functia get_gate_by_Id neimplementata")
    
    @abstractmethod
    def del_gate(self, gate_id: int) -> List[object]:
        raise NotImplementedError("Functia del_gate neimplementata")

    @abstractmethod
    def get_gates(self) -> List[object]:
        raise NotImplementedError("Functia get_gates neimplementata")
    
    @abstractmethod
    def put_gate(self, poarta: object) -> List[object]:
        raise NotImplementedError("Functia put_gate neimplementata")
    
    @abstractmethod
    def update_gate(self, gate_id: int, poarta: object) -> List[object]:
        raise NotImplementedError("Functia update_gate neimplementata")
    
    @abstractmethod
    def get_all_planes(self) -> List[object]:
        raise NotImplementedError("Functie get_all_planes neimplementata")
    
    @abstractmethod
    def get_plane_by_NrId(self, avion_Id: int) -> List[object]:
        raise NotImplementedError ("Functia get_plane_by_id neimplementata")
    
    @abstractmethod
    def put_plane(self, object: object) -> bool:
        raise NotImplementedError("Functia add_plane neimplementata")
    
    @abstractmethod
    def get_runway_by_id(self, runway_id: int) -> List[object]:
        raise NotImplementedError("Functia get_runway_by_id neimplementata")

    @abstractmethod
    def get_runways(self) -> List[object]:
        raise NotImplementedError("Functia get_runways neimplementata.")
    
    @abstractmethod 
    def put_runway(self, object:object) -> List[object]:
        raise NotImplementedError("Functia put_runway neimplementata.")
    
    @abstractmethod
    def del_runway_by_id(self, runway_id: int) -> List[object]:
        raise NotImplementedError("Functia del_runway neimplementata")
    
    @abstractmethod
    def get_history_by_NrId(self , nrIdentificare: str) -> List[object]:
        raise NotImplementedError("Fuctia get_history_by_NrId neimplementata")
    
class Singleton(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance