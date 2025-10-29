from sqlalchemy import Column, Integer, String, Float
from database import Base

class Veiculo(Base):
    __tablename__ = "veiculos"
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    motorizacao = Column(String, nullable=False)
    combustivel = Column(String, nullable=False)
    cor = Column(String, nullable=False)
    quilometragem = Column(Integer, nullable=False)
    portas = Column(Integer, nullable=False)
    transmissao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
