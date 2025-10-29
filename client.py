import socket
import json
import re
import unicodedata

Host= "127.0.0.1"
Port= 5000

def ev_requisicao(filtros):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((Host, Port))
            s.sendall(json.dumps(filtros).encode("utf-8"))
            data = b""
            while True:
                part = s.recv(4096)
                if not part:
                    break
                data += part
            resposta = data.decode("utf-8")

            try:
                return json.loads(resposta)
            except json.JSONDecodeError:
                print("Erro ao decodificar resposta do servidor.")
                return []

def acentos(mensagem):
    return ''.join(
        c for c in unicodedata.normalize('NFD', mensagem)
        if unicodedata.category(c) != 'Mn'
    ).lower()
def auto_agente(mensagem):
    mensagem = acentos(mensagem)
    filtros= {}
    marcas= ["toyota", "honda", "ford", "chevrolet", "volkswagen"]
    for m in marcas:
        if m in mensagem:
            filtros["marca"]= m.capitalize()

    combustiveis= ["gasolina", "diesel", "etanol", "flex"]
    for c in combustiveis:
        if c in mensagem:
            filtros["combustivel"]= c.capitalize()

    ano= re.search(r"\b(20[0-2][0-9]|10[8-9][0-9])\b", mensagem)
    if ano:
        filtros["ano"]= int(ano.group(1))

    cores = ["preto", "preta", "prata", "branco", "branca", "vermelho", "vermelha", "azul"]
    for cor in cores:
        if cor in mensagem:
            if cor in ["preta", "branca", "vermelha"]:
                base = cor[:-1] 
            else:
                base = cor
            filtros["cor"] = base.capitalize()

    transmissoes = ["manual", "automatica", "automático", "cvt"]
    for t in transmissoes:
        if "automatic" in t:
            if "automatic" in mensagem:
                filtros["transmissao"] = "Automática"
        elif t in mensagem:
            filtros["transmissao"] = t.capitalize()
    return filtros

def resultados(resultado):
    if not resultado:
        print("\n Nenhum veículo encontrado com esses critérios.\n")
        return
    print(f"\n {len(resultado)} Veículos encontrados:\n")
    for v in resultado[:10]:
        print(f"{v['marca']} {v['modelo']} {v['ano']} | "
              f"{v['cor']} | {v['combustivel']} | {v['transmissao']} | {v['quilometragem']} km | R$ {v['preco']:.2f}")
    print()

def agente():
    print("Olá! Eu sou seu assistente virtual de veículos C2S.")
    print("Exemplos do que você pode digitar:")
    print("--> 'Quero um Honda a Gasolina de 2020'")
    print("--> 'Procuro um Toyota Diesel'")
    print("--> 'Mostre carros flex da Volkswagen de cor branca'\n")
    while True:
        entrada= input("Você: ").strip()
        if entrada.lower() in ["sair", "exit", "tchau", "fechar", "finalizar", "encerrar"]:
            print("Até breve! Obrigado por usar o agente C2S.")
            break

        filtros= auto_agente(entrada)
        if not filtros:
            print("Não entendi muito bem..\n tente mencionar marca, ano ou combustível/transmissao.")
            continue
        print(f"\n Estou buscando veículos com filtros: {filtros}\n")

        resultado= ev_requisicao(filtros)
        resultados(resultado)

if __name__ == "__main__":
    agente()