from sqlalchemy.engine import Engine

from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class ExamQuestionModel(AbstractModel):
    # Table Name
    TABLE_NAME = 'qiz_exam_question'

    # Field Name
    ID = 'id'
    EXAM_ID = 'exam_id'
    QUESTION_ID = 'question_id'
    ANSWER_ID = 'answer_id'
    EXPLANATION_ID = 'explanation_id'

    def __init__(self, engine: Engine):
        self.engine = engine

    def table(self):
        self.table = \
            Table(self.TABLE_NAME, self.metaData,
              Column(self.ID, String(32), primary_key=True),
              Column(self.EXAM_ID, String(32), nullable=False),
              Column(self.QUESTION_ID, String(32), nullable=False),
              Column(self.ANSWER_ID, String(32), nullable=False),
              Column(self.EXPLANATION_ID, String(32), nullable=False)
              )

        return self
