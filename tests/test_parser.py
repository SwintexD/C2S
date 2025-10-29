from client import auto_agente

def test_parser_unico():
    f= auto_agente("Quero um Toyota 2017 a gasolina")
    assert f["marca"]== "Toyota"
    assert f["ano"]== 2017
    assert f["combustivel"].lower()== "gasolina"
def test_parser_multiplo():
    f=auto_agente("Gostaria de ver carros Volkswagen azul transmissão Automática e flex")
    assert f["marca"]== "Volkswagen"
    assert f["cor"]== "Azul"
    assert f["transmissao"]== "Automatica"
    assert f["combustivel"]== "Flex"