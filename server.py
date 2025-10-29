import socket
import json
from database import SessionL
from produtos import Veiculo
from query_engine import search


Host = "127.0.0.1"
Port = 5000

def buscar_veiculos(filtros):
    db= SessionL()
    try:
        results = search(db, filtros, limit=200)
        return [
            {
                "marca": v.marca,
                "modelo": v.modelo,
                "ano": v.ano,
                "cor": v.cor,
                "combustivel": v.combustivel,
                "quilometragem": v.quilometragem,
                "preco": v.preco,
                "transmissao": v.transmissao
            }
            for v in results
        ]
    finally:
        db.close()

def s_mcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, Port))
        s.listen()
        print(f"Servidor MCP rodando em {Host}:{Port}")

        while True:
            conn, addr= s.accept()
            with conn:
                data= conn.recv(4096).decode("utf-8")
                if not data:
                    break
                try:
                    filtros = json.loads(data)
                    resposta = buscar_veiculos(filtros)
                    conn.sendall(json.dumps(resposta, indent=2).encode("utf-8"))

                except Exception as e:
                    conn.sendall(json.dumps({"erro": str(e)}).encode("utf-8"))

if __name__== "__main__":
    s_mcp()

