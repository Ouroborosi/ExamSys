from sqlalchemy import MetaData
from sqlalchemy.engine import Engine


class AbstractModel():
    engine = None

    def __init__(self, engine=Engine):
        self.engine = engine

    def create(self):
        metaData = MetaData()

        metaData.create_all(self.engine)

        return self