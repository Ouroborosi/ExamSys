from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime

engine = create_engine('postgresql+psycopg2://pguser:p@localhost/quizdb', echo=True)
connection = engine.connect()

metadata = MetaData()
users = Table('users', metadata,
     Column('id', String(32), primary_key=True),
     Column('userName', String(64)),
     Column('password', String(64)),
     Column('fbUserId', String(32)),
     Column('fbAccessToken', String(128)),
     Column('createDate', DateTime),
     Column('modifiedDate', DateTime)
)

metadata.create_all(engine)