from faker import Faker
import random
from database import SessionL
from produtos import Veiculo

fakedb = Faker('pt_BR')

def gerar_dados(qtd=100):
    db = SessionL()

    marcas_modelos = {
        "Toyota": ["Corolla", "Yaris", "Hilux", "Etios"],
        "Honda": ["Civic", "HR-V", "Fit", "City"],
        "Ford": ["Ranger", "Mustang", "Fiesta", "Ka"],
        "Chevrolet": ["S10", "Tracker", "Onix", "Prisma"],
        "Volkswagen": ["Tiguan", "Golf", "Polo", "Fox"]
    }

    transmissoes = ["Manual", "Automática", "CVT"]
    combustiveis = ["Gasolina", "Diesel", "Etanol", "Flex"]
    cores = ["Preto", "Branco", "Prata", "Azul", "Vermelho"]

    for _ in range(qtd):
        marca = random.choice(list(marcas_modelos.keys()))
        modelo = random.choice(marcas_modelos[marca])
        ano = random.randint(1995, 2025)
        motorizacao = random.choice(["1.0", "1.3", "1.5", "2.0"])
        combustivel = random.choice(combustiveis)
        cor = random.choice(cores)
        quilometragem = random.randint(0, 300000)
        portas = random.choice([2, 4])
        transmissao = random.choice(transmissoes)
        preco = round(random.uniform(80000, 300000), 2)

        veiculo = Veiculo(
            marca = marca,
            modelo = modelo,
            ano = ano,
            motorizacao = motorizacao,
            combustivel = combustivel,
            cor = cor,
            quilometragem = quilometragem,
            portas = portas,
            transmissao = transmissao,
            preco = preco


        )
        db.add(veiculo)

    db.commit()
    db.close()
    print(f"{qtd} veículos inseridos com sucesso!")
    
if __name__ == "__main__":
    gerar_dados()