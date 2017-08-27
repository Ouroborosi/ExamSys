from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class ExplanationModel(AbstractModel):

    def table(self):
        self.table = \
            Table('qiz_explanation', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('answer_id', String(32), nullable=False),
              Column('explanation', String(4000), nullable=False)
              )

        return self