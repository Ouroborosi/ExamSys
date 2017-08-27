from sqlalchemy import MetaData, Table, Column, String, DateTime

from resources.modeling import AbstractModel

class UserModel(AbstractModel):

	def create(self):
		Table('users', self.metadata,
		  Column('id', String(32), primary_key=True),
		  Column('userName', String(64)),
		  Column('password', String(64)),
		  Column('fbUserId', String(32)),
		  Column('fbAccessToken', String(128)),
		  Column('createDate', DateTime),
		  Column('modifiedDate', DateTime)
		)

		return self
