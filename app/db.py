from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de la base de datos
DATABASE_URL = "mysql://oli:perrito0linn@localhost:3306/modulo2"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
