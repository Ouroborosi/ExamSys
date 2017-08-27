from sqlalchemy import Table, Column, String, DateTime

from resources.modeling import AbstractModel

class UserModel(AbstractModel):

	def table(self):
		Table('user', self.metadata,
		  Column('id', String(32), primary_key=True),
		  Column('userName', String(64), nullable=False),
		  Column('password', String(64), nullable=False),
		  Column('userId', String(32), nullable=False),
		  Column('accessToken', String(128), nullable=False),
		  Column('createDate', DateTime, nullable=False),
		  Column('modifiedDate', DateTime)
		)

		return self
