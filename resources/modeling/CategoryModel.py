from resources.modeling.AbstractModel import AbstractModel
from sqlalchemy import Table, Column, String

class CategoryModel(AbstractModel):

    def table(self):
        self.table = \
            Table('qiz_category', self.metadata,
              Column('id', String(32), primary_key=True),
              Column('category_name', String(50), nullable=False)
              )

        return self