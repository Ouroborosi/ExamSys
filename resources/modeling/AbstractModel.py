from sqlalchemy import MetaData
from sqlalchemy.engine import Engine
from abc import abstractmethod, ABCMeta


class AbstractModel(metaclass=ABCMeta):
    metaData = MetaData()

    def create(self):
        self.table()
        self.metaData.create_all(self.engine)

        return self

    @abstractmethod
    def table(self):
        pass