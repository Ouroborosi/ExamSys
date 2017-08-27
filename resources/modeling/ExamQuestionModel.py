from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class ExamQuestionModel(AbstractModel):

    def table(self):
        self.table = \
            Table('qiz_exam_question', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('exam_id', String(32), nullable=False),
              Column('question_id', String(32), nullable=False),
              Column('answer_id', String(32), nullable=False),
              Column('explanation_id', String(32), nullable=False)
              )

        return self
