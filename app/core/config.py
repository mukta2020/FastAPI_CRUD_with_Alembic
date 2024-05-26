# from dotenv import load_dotenv
# import os
from sqlalchemy import URL
# load_dotenv()

# # sqlite:///./test.db
# # db_url = os.environ.get("DB_URL")
# db_url = os.environ.get("sqlite:///home/sampleworking/py-api/TestDB.db")
# secret = os.environ.get("SECRET_KEY")
# algorithm = os.environ.get("ALGORITHM")
# access_token_time = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5433/Test"



# Assuming you have these variables defined
db_username = "postgres"
db_password = "1234"
host_server = "localhost"
db_server_port = 5433  # Assuming the default PostgreSQL port
database_name = "Test"
ssl_mode = "require"  # or "prefer" depending on your PostgreSQL configuration


# Create URL object
url_object = URL.create(    
   "postgresql",
    username=db_username,
    password=db_password,  # plain (unescaped) text
    host=host_server,
    port=db_server_port,
    database=database_name,
)

# Create URL object
url_object1 = URL.create(
    "postgresql",
    username=db_username,
    password=db_password,  # plain (unescaped) text
    host=host_server,
    database=database_name,
)
