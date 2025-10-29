import threading
import time
import socket
import json
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from produtos import Base, Veiculo
from query_engine import search

Host = "127.0.0.1"
Port = 6000

def sv_test():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    sample = [
        Veiculo(marca="Honda", modelo="Fit", ano=2014, motorizacao="1.6", combustivel="Etanol", cor="Prata", quilometragem=35000, portas=4, transmissao="Automática", preco=110000.0),
        Veiculo(marca="Toyota", modelo="Corolla", ano=2018, motorizacao="1.8", combustivel="Gasolina", cor="Prata", quilometragem=28000, portas=4, transmissao="Automática", preco=72500.0),
        Veiculo(marca="Ford", modelo="Ka", ano=2019, motorizacao="1.0", combustivel="Flex", cor="Vermelho", quilometragem=1350, portas=4, transmissao="Manual", preco=67000.0),
    ]
    session.add_all(sample)
    session.commit()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, Port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(4096).decode("utf-8")
            filtros = json.loads(data)
            results = search(session, filtros)
            response = [
                {
                    "marca": v.marca,
                    "modelo": v.modelo,
                    "ano": v.ano,
                    "combustivel": v.combustivel,
                    "cor": v.cor,
                    "transmissao": v.transmissao,
                    "quilometragem": v.quilometragem,
                    "preco": v.preco
                }
                for v in results
            ]
            conn.sendall(json.dumps(response).encode("utf-8"))
    session.close()

def test_mcp():
    server_thread = threading.Thread(target=sv_test, daemon=True)
    server_thread.start()
    time.sleep(0.5) 

    filtros = {"marca":"Ford", "ano":2019, "combustivel":"Flex"}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((Host, Port))
        s.sendall(json.dumps(filtros).encode("utf-8"))
        resposta = s.recv(8192).decode("utf-8")
        resultados = json.loads(resposta)

    assert len(resultados) == 1
    assert resultados[0]["marca"] == "Ford"
    assert resultados[0]["ano"] == 2019
    assert resultados[0]["combustivel"] == "Flex"

