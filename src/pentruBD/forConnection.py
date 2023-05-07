from typing import List
import sqlalchemy as sqlal
from datetime import datetime,date
from model.modelAvion import Avion
from utility.Decorator import singleton
from storage.base import StorageObject
from model.modelAvion import Avion


@singleton
class airportBD(StorageObject):
    def __init__(self):
        self.listAvioane=[]
        pass
    
    # def get_all_planes(self) -> List[Avion]:
    #     #try:
    #         print(1)
    #         url = 'mysql+pymysql://root:@localhost/proiectavioane'
    #         print(2)
    #         engine = sqlal.create_engine(url)
    #         print(3)
            # conn = engine.connect()
            # print(4)
            # table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=engine)
            # print(5)
            # sql = sqlal.select(table.columns)
            # print(6)
            # result = conn.execute(sql)
            # print(7)
        #     for row in result:
        #         idUnic= row[0]
        #         numeAvion = row[1]
        #         model = row[2]
        #         avion=Avion(idUnic,numeAvion,model)
        #         self.listAvioane.append(avion)
        # except Exception as e:
        #     print("Probleme la functia get_all_planes.")
        #     print(e)
        # finally:
        #     #self.closeAll(conn,engine)
        #     return self.listAvioane
        
    

    def historyRegister(self,avion: object, poarta: object):
        try:
            url = 'mysql+pymysql://root:@localhost/proiectavioane'
            engine = sqlal.create_engine(url)
            conn = engine.connect()
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=engine)
            sql = sqlal.select(table.columns.Avion_NrIdentificare).where(table.columns.Avion_NrIdentificare==avion.IdNum.upper())
            result = conn.execute(sql)
            if result.first() is None:
                sql = sqlal.insert(table).values(Avion_NrIdentificare=avion.IdNum.upper(),Avion_Model=avion.Model)
                conn.execute(sql)
                conn.commit()
            table = sqlal.Table('istoric', sqlal.MetaData(), autoload_with=engine)
            pista = int(avion.Pista)
            dataAzi = date.today()
            sql = sqlal.insert(table).values(
            Avion_Id=avion.IdNum.upper(),
            tipZbor=avion.tip_zbor,
            sursa=avion.sursa,
            destinatia=avion.destinatia,
            motiv=avion.motiv,
            dataAterizare=dataAzi,
            oraAterizare = datetime.now().time(),
            poarta=poarta.nrReferinta,
            pistaFolosita=pista)
            conn.execute(sql)
            conn.commit()
        except Exception as e:
            print("Eroare la introducerea in baza de date")
            print (e)
        finally:
            self.closeAll(conn,engine)
        
    def insertAvionBD(avion: object):
        try:
            url = 'mysql+pymysql://root:@localhost/proiectavioane'
            engine = sqlal.create_engine(url)
            conn = engine.connect()
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=engine)
            sql = sqlal.select(table.columns.Avion_NrIdentificare).where(table.columns.Avion_NrIdentificare==avion.IdNum.upper())
            result = conn.execute(sql)
            if result.first() is None:
                sql = sqlal.insert(table).values(Avion_NrIdentificare=avion.IdNum,Avion_Model=avion.Model)
                conn.execute(sql)
                conn.commit()
                airportBD.closeAll(conn, engine)
                return True
            else:
                airportBD.closeAll(conn, engine)
                return False
        except Exception as e:
            print("Problema la inserare in tabela avioane")
            print(e)
        finally:
            airportBD.closeAll(conn,engine)

    def plecareAvion(self,avion: object):
        try:
            url = 'mysql+pymysql://root:@localhost/proiectavioane'
            engine = sqlal.create_engine(url)
            conn = engine.connect()
            table = sqlal.Table('istoric', sqlal.MetaData(), autoload_with=engine)
            sql = sqlal.select(table.columns).where(table.columns.Avion_Id==avion.IdNum.upper()).order_by(table.columns.Istoric_Id.desc()) 
            result = conn.execute(sql)
            row = result.fetchone()
            istoric_id = row[0]
            sql = sqlal.update(table).where(table.columns.Istoric_Id == istoric_id).values(dataPlecare=date.today(),
            oraPlecare=datetime.now().time())
            conn.execute(sql)
            conn.commit()
        except Exception as e:
            print("Exceptie la data si ora de plecare.")
            print(e)
        finally:
            self.closeAll(conn,engine)

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








    

