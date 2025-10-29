from database import Base, engine
from produtos import Veiculo

print("Criando banco de dados..")
Base.metadata.create_all(bind=engine)
print("Banco de dados criado com sucesso!")

