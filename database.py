import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['DATABASE_USER']}:@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}"

####################################################################################
#Lectura de las varibales de entorno
####################################################################################
user = os.environ['DATABASE_USER']
password = os.environ['DATABASE_PASSWORD']
host = os.environ['DATABASE_HOST']
port = os.environ['DATABASE_PORT']
db_name = os.environ['DATABASE_NAME']

####################################################################################
#Construccion del URL.
####################################################################################
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

####################################################################################
#Creamos la conexion principal a la base de datos.
####################################################################################
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

####################################################################################
#Creamos la sesion local.
####################################################################################
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

####################################################################################
#Creamos la base de los siguinetes modelos.
####################################################################################
Base = declarative_base()