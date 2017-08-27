from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String, DateTime


class ExamModuleModel(AbstractModel):

    def table(self):
        self.table = \
            Table('qiz_exam_module', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('description', String(4000), nullable=False),
              Column('user_id', String(32), nullable=False),
              Column('create_date', DateTime, nullable=False),
              Column('modified_date', DateTime, nullable=True)
              )

        return self