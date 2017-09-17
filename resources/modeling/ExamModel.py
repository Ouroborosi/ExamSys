from sqlalchemy import Table, Column, String
from sqlalchemy.engine import Engine

from resources.modeling.AbstractModel import AbstractModel


class ExamModel(AbstractModel):
    # Table Name
    TABLE_NAME = 'qiz_exam'

    # Field Name
    ID = 'id'
    USER_ID = 'user_id'
    MODULE_ID = 'module_id'

    def __init__(self, engine: Engine):
        self.engine = engine

    def table(self):
        self.table = \
            Table(self.TABLE_NAME, self.metaData,
              Column(self.ID, String(32), primary_key=True),
              Column(self.USER_ID, String(32), nullable=False),
              Column(self.MODULE_ID, String(32), nullable=False)
              )

        return self