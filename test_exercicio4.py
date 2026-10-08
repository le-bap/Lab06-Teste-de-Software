
import pytest

def tem_frete_gratis(valor_compra, cliente_premium, peso):
    if valor_compra >= 200 and cliente_premium and peso <= 30:
        return True
    return False

@pytest.mark.parametrize(
    "valor_compra, cliente_premium, peso, esperado",
    [
        pytest.param(200, True, 30, True, id="R1"),
        pytest.param(200, True, 31, False, id="R2"),
        pytest.param(200, False, 30, False, id="R3"),
        pytest.param(200, False, 31, False, id="R4"),
        pytest.param(199, True, 30, False, id="R5"),
        pytest.param(199, True, 31, False, id="R6"),
        pytest.param(199, False, 30, False, id="R7"),
        pytest.param(199, False, 31, False, id="R8"),
    ]
)
def test_tem_frete_gratis(valor_compra, cliente_premium, peso, esperado):
    assert tem_frete_gratis(valor_compra, cliente_premium, peso) == esperado


# | Regra | Compra >= RS200 | Cliente premium | Peso ≤ 30 kg | Resultado |
# | ----- | --------------- | --------------- | ------------ | ------------- |
# | R1    | F               | -               | -            | Frete cobrado |
# | R2    | V               | F               | -            | Frete cobrado |
# | R3    | V               | V               | F            | Frete cobrado |
# | R4    | V               | V               | V            | Frete grátis  |

# R1: se a compra não atingir R$ 200, não importa se o cliente é premium nem qual é o peso.
# R2: se a compra atingir R$ 200, mas o cliente não for premium, o peso deixa de importar.
# R3: se a compra atingir R$ 200 e o cliente for premium, mas o pedido pesar mais de 30 kg, o frete será cobrado.
# R4: se as três condições forem verdadeiras, o frete será grátis.