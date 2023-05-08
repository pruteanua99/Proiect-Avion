from typing import List
import sqlalchemy as sqlal
from datetime import datetime,date
from model.modelAvion import Avion
from utility.Decorator import singleton
from storage.base import StorageObject
from model.modelGate import Gate
from model.modelHistory import History
from model.modelRunway import runway


@singleton
class airportBD(StorageObject):
    def __init__(self):
        self.listaAvioane = []
        self.listaPiste = []
        self.listaPorti = []
        self.listaIstoric = []
        self.url = 'mysql+pymysql://root:@localhost/proiectavioane'
        self.engine = sqlal.create_engine(self.url)
        self.conn = self.engine.connect()
    #region mainUsage
    def historyRegister(self,avion: object, poarta: object) -> None:
        try:
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns.Avion_NrIdentificare).where(table.columns.Avion_NrIdentificare==avion.IdNum.upper())
            result = self.conn.execute(sql)
            if result.first() is None:
                sql = sqlal.insert(table).values(Avion_NrIdentificare=avion.IdNum.upper(),Avion_Model=avion.Model)
                self.conn.execute(sql)
                self.conn.commit()
            table = sqlal.Table('istoric', sqlal.MetaData(), autoload_with=self.engine)
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
            self.conn.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Eroare la introducerea in baza de date")
            print (e)
    def insertAvionBD(self,avion: object) -> bool:
        try:
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns.Avion_NrIdentificare).where(table.columns.Avion_NrIdentificare==avion.IdNum.upper())
            result = self.conn.execute(sql)
            if result.first() is None:
                sql = sqlal.insert(table).values(Avion_NrIdentificare=avion.IdNum,Avion_Model=avion.Model)
                self.conn.execute(sql)
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Problema la inserare in tabela avioane")
            print(e)
    def plecareAvion(self,avion: object) -> None:
        try:
            table = sqlal.Table('istoric', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns).where(table.columns.Avion_Id==avion.IdNum.upper()).order_by(table.columns.Istoric_Id.desc()) 
            result = self.conn.execute(sql)
            row = result.fetchone()
            istoric_id = row[0]
            sql = sqlal.update(table).where(table.columns.Istoric_Id == istoric_id).values(dataPlecare=date.today(),
            oraPlecare=datetime.now().time())
            self.conn.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Exceptie la data si ora de plecare.")
            print(e)
    #endregion
    #region PlaneMethods
    def get_all_planes(self) -> List[Avion]:
        self.listaAvioane.clear()
        try:
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns)
            result = self.conn.execute(sql)
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
            return self.listaAvioane
    def get_plane_by_NrId(self, avion_Id: int) -> List[Avion]:
        self.listaAvioane.clear()
        try:
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns).where(table.columns.Avion_Id==avion_Id)
            result = self.conn.execute(sql)
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
            return self.listaAvioane
    def put_plane(self, avion: Avion) -> List[Avion]:
        self.listaAvioane.clear()
        try:
            table = sqlal.Table('avioane', sqlal.MetaData(), autoload_with=self.engine)
            sql=sqlal.insert(table).values(Avion_NrIdentificare=avion.nrIdentificare,Avion_Model=avion.model)
            self.conn.execute(sql)
            self.conn.commit()
            self.listaAvioane.append(avion)
        except Exception as e:
            print("Problema la inserare in tabela avioane")
            print(e)
        finally:
            return self.listaAvioane
    #endregion
    #region RunwayMethods
    def put_runway(self, pista: runway) -> List[runway]:
        self.listaPiste.clear()
        try:
            url = 'mysql+pymysql://root:@localhost/proiectavioane'
            engine = sqlal.create_engine(url)
            conn = engine.connect()
            table = sqlal.Table('piste', sqlal.MetaData(), autoload_with=engine)
            sql=sqlal.insert(table).values(Pista_Id=pista.id_runway)
            conn.execute(sql)
            conn.commit()
            self.listaPiste.append(pista)
        except Exception as e:
            print("Problema la inserare in tabela piste")
            print(e)
        finally:
            return self.listaPiste
    def get_runways(self) -> List[runway]:
        self.listaPiste.clear()
        try:
            table = sqlal.Table('piste', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns)
            result = self.conn.execute(sql)
            for row in result:
                idUnic= row[0]
                pista=runway(id_runway=idUnic)
                self.listaPiste.append(pista)
        except Exception as e:
            print("Problema la metodaa get_runways.")
            print(e)
        finally:
            return self.listaPiste
    def get_runway_by_id(self, runway_id: int) -> List[runway]:
        self.listaPiste.clear()
        try:
            table = sqlal.Table('piste', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns).where(table.columns.Pista_Id==runway_id)
            result = self.conn.execute(sql)
            for row in result:
                idUnic= row[0]
                pista=runway(id_runway=idUnic)
                self.listaPiste.append(pista)
        except Exception as e:
            print("Problema la metodaa get_runways.")
            print(e)
        finally:
            return self.listaPiste
    def del_runway_by_id(self, runway_id: int) -> List[runway]:
        self.listaPiste.clear()
        try:
            table = sqlal.Table('piste', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns).where(table.columns.Pista_Id==runway_id)
            result = self.conn.execute(sql)
            for row in result:
                idUnic= row[0]
                pista=runway(id_runway=idUnic)
                self.listaPiste.append(pista)
            sql=sqlal.delete(table).where(table.columns.Pista_Id==runway_id)
            self.conn.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("problema la stergere pista.")
            print(e)
        finally:
            return self.listaPiste
    #endregion
    #region GateMethods
    def get_gates(self,) -> List[Gate]:
        self.listaPorti.clear()
        try:
            table=sqlal.Table('porti',sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns)
            result = self.conn.execute(sql)
            for row in result:
                idUnic= row[1]
                descriere = row[0]
                poarta=Gate(Poarta_fel=descriere,Poarta_Referinta=idUnic)
                self.listaPorti.append(poarta)
        except Exception as e:
            print("Problema la get_gates.")
            print(e)
        finally:
            return self.listaPorti
    def get_gate_by_Id(self, gate_id: int) -> List[Gate]:
        self.listaPorti.clear()
        try:
            table=sqlal.Table('porti',sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns).where(table.columns.Poarta_Referinta==gate_id)
            result = self.conn.execute(sql)
            for row in result:
                idUnic= row[1]
                descriere = row[0]
                poarta=Gate(Poarta_fel=descriere,Poarta_Referinta=idUnic)
            self.listaPorti.append(poarta)
        except Exception as e:
            print("Problema la get_gates.")
            print(e)
        finally:
            return self.listaPorti
    def put_gate(self, poarta: Gate) -> List[Gate]:
        self.listaPorti.clear()
        try:
            table=sqlal.Table('porti',sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.insert(table).values(Poarta_Fel=poarta.Poarta_fel, Poarta_Referinta=poarta.Poarta_Referinta)
            self.conn.execute(sql)
            self.conn.commit()
            self.listaPorti.append(poarta)
        except Exception as e:
            print("Problema la put_gates.")
            print(e)
        finally:
            return self.listaPorti   
    def del_gate(self, gate_id: int) -> List[Gate]:
        self.listaPorti.clear()
        try:
            table = sqlal.Table('porti',sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns).where(table.columns.Poarta_Referinta==gate_id)
            result = self.conn.execute(sql)
            for row in result:
                idUnic= row[1]
                descriere = row[0]
                poarta=Gate(Poarta_fel=descriere,Poarta_Referinta=idUnic)
                self.listaPorti.append(poarta)
            sql=sqlal.delete(table).where(table.columns.Poarta_Referinta==gate_id)
            self.conn.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Problema la del_gate")
            print(e)
        finally:
            return self.listaPorti
    def update_gate(self, gate_id: int, poarta: Gate) -> List[Gate]:
        self.listaPorti.clear()
        try:
            table = sqlal.Table('porti',sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.update(table).where(table.columns.Poarta_Referinta==gate_id).values(Poarta_Fel=poarta.Poarta_fel)
            self.conn.execute(sql)
            self.conn.commit()
            self.listaPorti.append(poarta)
        except Exception as e:
            print("Problema la update_gate")
            print(e)
        finally:
            return self.listaPorti
    #endregion
    #region HistoryMethods
    def get_history_by_NrId(self, nrIdentificare: str) -> List[History]:
        self.listaIstoric.clear()
        try:
            table = sqlal.Table('istoric', sqlal.MetaData(), autoload_with=self.engine)
            sql = sqlal.select(table.columns).where(table.columns.Avion_Id==nrIdentificare)
            result = self.conn.execute(sql)
            for row in result:
                istoric_Id = row[0]
                numeAvion = row[1]
                tipZborr = row[2]
                sursaa = row[3]
                destinatiaa = row[4]
                motivv = row[5]
                dataAterizaree = row[6]
                dataPlecaree = row[7]
                poartaa = row[8]
                pistaFolositaa = row[9]
                oraPlecaree = row[10]
                oraAterizaree = row[11]
                istoric=History(Istoric_Id = istoric_Id,Avion_Id=numeAvion,tipZbor=tipZborr,sursa=sursaa,destinatia=destinatiaa, motiv=motivv,
                                poarta=poartaa,pistaFolosita=pistaFolositaa,dataAterizare=dataAterizaree,dataPlecare=dataPlecaree,oraPlecare=oraPlecaree, oraAterizare=oraAterizaree)
                self.listaIstoric.append(istoric)
        except Exception as e:
            print("Problema la get_history_by_NrId.")
            print(e)
        finally:
            return self.listaIstoric
    #endregion
