from sqlalchemy import Table, Column, String, DateTime

from resources.modeling import AbstractModel

class UserModel(AbstractModel):

	def table(self):
		self.table = \
			Table('qiz_user', self.metadata,
			  Column('id', String(32), primary_key=True),
			  Column('user_name', String(64), nullable=False),
			  Column('password', String(64), nullable=False),
			  Column('user_id', String(32), nullable=False),
			  Column('access_token', String(128), nullable=False),
			  Column('create_date', DateTime, nullable=False),
			  Column('modified_date', DateTime, nullable=True)
			)

		return self
