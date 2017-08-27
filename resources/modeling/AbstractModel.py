from sqlalchemy import MetaData
from sqlalchemy.engine import Engine
from abc import abstractmethod

class AbstractModel():
    engine = None

    def __init__(self, engine: Engine):
        self.engine = engine

    def create(self):
        metaData = MetaData()
        self.table()
        metaData.create_all(self.engine)

        return self

    @abstractmethod
    def table(self):
        pass