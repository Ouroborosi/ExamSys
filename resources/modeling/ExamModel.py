from sqlalchemy import Table, Column, String, DateTime

from resources.modeling.AbstractModel import AbstractModel


class ExamModel(AbstractModel):

    def table(self):
        Table('exam', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('userId', String(32), nullable=False)
              )

        return self