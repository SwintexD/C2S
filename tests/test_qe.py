import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from produtos import Base, Veiculo
from query_engine import search
@pytest.fixture

def memory_session():
    engine=create_engine("sqlite:///:memory:", connect_args={"checK_same_thread": False})
    Base.matadata.create_all(bind=engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    sample = [
        Veiculo(marca="Chevrolet", modelo="Prisma", ano=2010, motorizacao="2.0", combustivel="Flex", cor="Branco", quilometragem=79300, portas=4, transmissao="Automática", preco=125500.0),
        Veiculo(marca="Toyota", modelo="Corolla", ano=2018, motorizacao="1.8", combustivel="Gasolina", cor="Prata", quilometragem=80000, portas=4, transmissao="Automática", preco=99900.0),
        Veiculo(marca="Ford", modelo="Ka", ano=2020, motorizacao="1.0", combustivel="Flex", cor="Vermelho", quilometragem=30000, portas=4, transmissao="Manual", preco=45000.0),
    ]
    session.add.all(sample)
    session.commit()
    yield session
    session.close()

def search_marca(memory_session):
    res = search(memory_session, {"marca":"Chevrolet"})
    assert len(res) == 1
    assert res[0].marca == "Chevrolet"

def search_ano_combus(memory_session):
    res = search(memory_session, {"ano":2010, "combustivel":"Flex"})
    assert len(res) == 2
    marcas = {v.marca for v in res}
    assert "Chevrolet" in marcas and "Ford" in marcas

def range_preco(memory_session):
    res = search(memory_session, {"max_price":100000})
    assert all(v.preco <= 100000 for v in res)
