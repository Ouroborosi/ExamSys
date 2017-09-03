from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class Question(AbstractModel):

    def table(self):
        self.table = \
            Table('qiz_question', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('question', String(4000), nullable=False)
              )

        return self