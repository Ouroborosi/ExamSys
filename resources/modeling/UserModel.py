from sqlalchemy import Table, Column, String, DateTime
from sqlalchemy.engine import Engine

from resources.modeling import AbstractModel

class UserModel(AbstractModel):
	# Table Name
	TABLE_NAME = 'qiz_user'

	# Field Name
	ID = 'id'
	USER_NAME = 'user_name'
	PASSWORD = 'password'
	USER_ID = 'user_id'
	ACCESS_TOKEN = 'access_token'
	CREATE_DATE = 'create_date'
	MODIFIED_DATE = 'modified_date'

	# def __init__(self, engine:Engine):
	# 	self.engine = engine

	def table(self):
		self.table = \
			Table(self.TABLE_NAME, self.metaData,
			  Column(self.ID, String(32), primary_key=True),
			  Column(self.USER_NAME, String(64), nullable=False),
			  Column(self.PASSWORD, String(64), nullable=False),
			  Column(self.USER_ID, String(32), nullable=False),
			  Column(self.ACCESS_TOKEN, String(128), nullable=False),
			  Column(self.CREATE_DATE, DateTime, nullable=False),
			  Column(self.MODIFIED_DATE, DateTime, nullable=True)
			)

		return self