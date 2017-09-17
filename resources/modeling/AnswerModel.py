from sqlalchemy.engine import Engine

from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String, ForeignKey


class AnswerModel(AbstractModel):
    # Table Name
    TABLE_NAME = 'qiz_answer'

    # Field Name
    ID = 'id'
    QUESTION_ID = 'question_id'
    ANSWER = 'answer'

    def __init__(self, engine: Engine):
        self.engine = engine

    def table(self):
        self.table = \
            Table(self.TABLE_NAME, self.metaData,
                  Column(self.ID, String(32), primary_key=True),
                  Column(self.QUESTION_ID, String(32), ForeignKey('qiz_question.id'), nullable=False),
                  Column(self.ANSWER, String(4000), nullable=False)
                  )

        return self.table