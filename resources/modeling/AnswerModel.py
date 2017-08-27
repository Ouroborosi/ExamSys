from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class AnswerModel(AbstractModel):

    def table(self):
        self.table = \
            Table('qiz_answer', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('question_id', String(32), nullable=False),
              Column('answer', String(4000), nullable=False)
              )

        return self