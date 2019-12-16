from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, func, String

engine = create_engine("mysql://root:@localhost/codingthunder")
db_session = scoped_session(sessionmaker(autocommit=False,autoflush = False, bind=engine))
base = declarative_base()
base.query = db_session.query_property()


class App(base):
	__tablename__ = "app"
	Id = Column(Integer, primary_key=True)
	title= Column(String(100), nullable=False)
	description = Column(String(100), nullable=False)
	done = Column(String(100),nullable = False)
