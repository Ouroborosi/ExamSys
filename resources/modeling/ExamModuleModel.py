from sqlalchemy.engine import Engine

from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String, DateTime


class ExamModuleModel(AbstractModel):
    # Table Name
    TABLE_NAME = 'qiz_exam_module'

    # Field Name
    ID = 'id'
    DESCRIPTION = 'description'
    USER_ID = 'user_id'
    CATEGORY_ID = 'category_id'
    CREATE_DATE = 'create_date'
    MODIFIED_DATE = 'modified_date'

    def table(self):
        self.table = \
            Table(self.TABLE_NAME, self.metaData,
              Column(self.ID, String(32), primary_key=True),
              Column(self.DESCRIPTION, String(4000), nullable=False),
              Column(self.USER_ID, String(32), nullable=False),
              Column(self.CATEGORY_ID, String(32), nullable=False),
              Column(self.CREATE_DATE, DateTime, nullable=False),
              Column(self.MODIFIED_DATE, DateTime, nullable=True)
            )

        return self