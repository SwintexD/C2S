from sqlalchemy.orm import Session
from produtos import Produto

def criar_produto(db: Session, nome: str, preco: float, quantidade: int, descricao: str = None):
    novo_produto = Produto(
        nome=nome,
        preco=preco,
        quantidade=quantidade,
        descricao=descricao     
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def listar_produtos(db: Session):
    return db.query(Produto).all()

def buscar_produto_por_nome(db: Session, nome: str):
    return db.query(Produto).filter(Produto.nome(f"%{nome}%")).all()

def atualizar_produto(db: Session, produto_id: int, novos_dados: dict):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        return None

    for chave, valor in novos_dados.items():
        setattr(produto, chave, valor)
    db.commit()
    db.refresh(produto)
    return produto

def deletar_produto(db: Session, produto_id, int):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return True
    return False
