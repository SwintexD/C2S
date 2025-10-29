from sqlalchemy.orm import Session
from produtos import Veiculo

def qBuild(session: Session, filtros: dict):
    query= session.query(Veiculo)
    if not filtros:
        return query
    
    if "marca" in filtros:
        query= query.filter(Veiculo.marca.ilike(f"%{filtros['marca']}%"))
    
    if "ano" in filtros:
        try:
            query= query.filter(Veiculo.ano==int(filtros["ano"]))
        except ValueError:
            pass
    if "combustivel" in filtros:
        query=query.filter(Veiculo.combustivel.ilike(f"%{filtros['combustivel']}%"))

    if "cor" in filtros:
        query=query.filter(Veiculo.cor.ilike(f"%{filtros['cor']}%"))
    if "transmissao" in filtros:
        query=query.filter(Veiculo.transmissao.ilike(f"%{filtros['transmissao']}%"))
    if "max_price" in filtros:
        try:
            query=query.filter(Veiculo.preco<=float(filtros["max_price"]))
        except ValueError:
            pass
    if "min_price" in filtros:
        try:
            query=query.filter(Veiculo.preco>=float(filtros["min_price"]))
        except ValueError:
            pass
    return query

def search(session: Session, filtros: dict, limit: int=100):
    q= qBuild(session, filtros)
    return q.limit(limit).all()