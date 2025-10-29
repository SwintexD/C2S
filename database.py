from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///produtos.db", future=True, echo=False)
SessionL = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)