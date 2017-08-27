from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime

from resources.modeling.AbstractModel import AbstractModel
from resources.modeling.UserModel import UserModel

engine = create_engine('postgresql+psycopg2://pguser:p@localhost/quizdb', echo=True)
connection = engine.connect()

abstractModel = AbstractModel().__init__(engine)
UserModel().create()



