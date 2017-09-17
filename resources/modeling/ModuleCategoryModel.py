from sqlalchemy.engine import Engine

from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class ModuleCategoryModel(AbstractModel):
    # Table Name
    TABLE_NAME = 'qiz_module_category'

    # Field Name
    ID = 'id'
    CATEGORY_NAME = 'category_name'

    def __init__(self, engine: Engine):
        self.engine = engine

    def table(self):
        self.table = \
            Table(self.TABLE_NAME, self.metaData,
              Column(self.ID, String(32), primary_key=True),
              Column(self.CATEGORY_NAME, String(50), nullable=False)
            )

        return self