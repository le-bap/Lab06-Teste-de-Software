from IMC import calcular_imc, categorizar_imc, classificar_pessoa

def test_abaixo_do_peso():
    assert categorizar_imc(18.0) == "abaixo do peso"


def test_peso_normal():
    assert categorizar_imc(22.0) == "peso normal"


def test_sobrepeso():
    assert categorizar_imc(27.0) == "sobrepeso"


def test_obesidade():
    assert categorizar_imc(32.0) == "obesidade"

