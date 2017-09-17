from sqlalchemy.engine import Engine

from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class ExplanationModel(AbstractModel):
    # Table Name
    TABLE_NAME = 'qiz_explanation'

    # Field Name
    ID = 'id'
    ANSWER_ID = 'answer_id'
    EXPLANATION = 'explanation'

    def table(self):
        self.table = \
            Table(self.TABLE_NAME, self.metaData,
              Column(self.ID, String(32), primary_key=True),
              Column(self.ANSWER_ID, String(32), nullable=False),
              Column(self.EXPLANATION, String(4000), nullable=False)
              )

        return self