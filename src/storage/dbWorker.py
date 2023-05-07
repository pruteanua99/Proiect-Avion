from .base import StorageObject, Singleton
import sqlalchemy as sqlal
from typing import List
from model import Avion

class dbWorker(StorageObject,Singleton):
    
    def __init__ (self):
        self.listaAvioane = []
    
    def get_all_planes(self) -> List[Avion]:
        self.listaAvioane.clear()
        try:
            url = 'mysql+pymysql://root:@localhost/proiectavioane'
            engine = sqlal.create_engine(url)
            conn = engine.connect()
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=engine)
            sql = sqlal.select(table.columns)
            result = conn.execute(sql)
            for row in result:
                idUnic= row[0]
                numeAvion = row[1]
                modell = row[2]
                avion=Avion(avion_id=idUnic,nrIdentificare=numeAvion,model=modell)
                self.listaAvioane.append(avion)
        except Exception as e:
            print("Probleme la functia get_all_planes.")
            print(e)
        finally:
            self.closeAll(conn,engine)
            return self.listaAvioane
        
    def get_plane_by_NrId(self, avion_Id: int) -> List[Avion]:
        self.listaAvioane.clear()
        try:
            url = 'mysql+pymysql://root:@localhost/proiectavioane'
            engine = sqlal.create_engine(url)
            conn = engine.connect()
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=engine)
            sql = sqlal.select(table.columns).where(table.columns.Avion_Id==avion_Id)
            result = conn.execute(sql)
            for row in result:
                idUnic= row[0]
                numeAvion = row[1]
                modell = row[2]
                avion=Avion(avion_id=idUnic,nrIdentificare=numeAvion,model=modell)
                self.listaAvioane.append(avion)
        except Exception as e:
            print("Probleme la functia get_all_planes.")
            print(e)
        finally:
            self.closeAll(conn,engine)
            return self.listaAvioane
        
    def put_plane(self, avion: Avion) -> List[Avion]:
        self.listaAvioane.clear()
        try:
            url = 'mysql+pymysql://root:@localhost/proiectavioane'
            engine = sqlal.create_engine(url)
            conn = engine.connect()
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=engine)
            sql=sqlal.insert(table).values(Avion_NrIdentificare=avion.nrIdentificare,Avion_Model=avion.model)
            conn.execute(sql)
            conn.commit()
            sql=sqlal.select(table.columns).where(Avion_NrIdentificare=avion.nrIdentificare)
            result=conn.execute(sql)
            for row in result:
                idUnic= row[0]
                numeAvion = row[1]
                modell = row[2]
                avion=Avion(avion_id=idUnic,nrIdentificare=numeAvion,model=modell)
                self.listaAvioane.append(avion)
        except Exception as e:
            print("Problema la inserare in tabela avioane")
            print(e)
        finally:
            self.closeAll(conn,engine)   
            return self.listaAvioane

    def closeAll(self,conn: object, engine: object):
        try:
            if conn is not None:
                conn.close()
        except Exception as e:
            print("Problema la inchiderea conexiunii...")
            print(e)
        try:
            if engine is not None:
                engine.dispose()
        except Exception as e:
            print("Problema la inchiderea engine...")
            print(e)



