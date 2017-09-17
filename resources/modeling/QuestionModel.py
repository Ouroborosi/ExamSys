from sqlalchemy.engine import Engine

from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class Question(AbstractModel):
    # Table Name
    TABLE_NAME = 'qiz_question'

    # Field Name
    ID = 'id'
    QUESTION = 'question'

    def __init__(self, engine: Engine):
        self.engine = engine

    def table(self):
        self.table = \
            Table(self.TABLE_NAME, self.metaData,
              Column(self.ID, String(32), primary_key=True),
              Column(self.QUESTION, String(4000), nullable=False)
              )

        return self