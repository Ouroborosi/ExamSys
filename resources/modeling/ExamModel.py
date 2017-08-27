from sqlalchemy import Table, Column, String

from resources.modeling.AbstractModel import AbstractModel


class ExamModel(AbstractModel):

    def table(self):
        self.table = \
            Table('qiz_exam', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('user_id', String(32), nullable=False),
              Column('module_id', String(32), nullable=False)
              )

        return self