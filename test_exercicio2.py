import pytest
from IMC import calcular_imc, categorizar_imc, classificar_pessoa


@pytest.mark.parametrize(
    "imc, esperado",
    [
        pytest.param(18.499, "abaixo do peso", id="abaixo-18.5"),
        pytest.param(18.5, "peso normal", id="fronteira-18.5"),
        pytest.param(18.501, "peso normal", id="acima-18.5"),
        pytest.param(24.999, "peso normal", id="abaixo-25"),
        pytest.param(25.0, "sobrepeso", id="fronteira-25"),
        pytest.param(25.001, "sobrepeso", id="acima-25"),
        pytest.param(29.999, "sobrepeso", id="abaixo-30"),
        pytest.param(30.0, "obesidade", id="fronteira-30"),
        pytest.param(30.001, "obesidade", id="acima-30"),
    ]
)
def test_categorizar_imc_valores_limite(imc, esperado):
    assert categorizar_imc(imc) == esperado

