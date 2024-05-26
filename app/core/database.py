from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from core.config import url_object
from sqlalchemy import URL

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5433/Test"

# engine = create_engine(	SQLALCHEMY_DATABASE_URL )

print('url-----')

url_object = URL.create(    
   "postgresql",
    username='postgres',
    password='1234',  
    host='localhost',
    port=5433,
    database='drugdbdev',
)
engine = create_engine(	url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
