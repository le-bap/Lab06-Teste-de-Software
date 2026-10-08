import pytest
from IMC import classificar_vento

@pytest.mark.parametrize(
    "velocidade, esperado",
    [
        pytest.param(10, "calmo", id="vento-calmo"),
        pytest.param(30, "moderado", id="vento-moderado"),
        pytest.param(50, "forte", id="vento-forte"),
        pytest.param(70, "tempestade", id="vento-tempestade"),
    ]
)
def test_classes_equivalencia_vento(velocidade, esperado):
    assert classificar_vento(velocidade) == esperado

@pytest.mark.parametrize(
    "velocidade, esperado",
    [
        pytest.param(19.999, "calmo", id="abaixo-20"),
        pytest.param(20, "moderado", id="limite-20"),
        pytest.param(20.001, "moderado", id="acima-20"),

        pytest.param(39.999, "moderado", id="abaixo-40"),
        pytest.param(40, "forte", id="limite-40"),
        pytest.param(40.001, "forte", id="acima-40"),

        pytest.param(59.999, "forte", id="abaixo-60"),
        pytest.param(60, "tempestade", id="limite-60"),
        pytest.param(60.001, "tempestade", id="acima-60"),
    ]
)
def test_valores_limite_vento(velocidade, esperado):
    assert classificar_vento(velocidade) == esperado
