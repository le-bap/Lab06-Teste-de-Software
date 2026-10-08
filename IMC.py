def classificar_por_faixas(valor, faixas):
    for limite_superior, rotulo in faixas:
        if valor < limite_superior:
            return rotulo


def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser positivos")

    return peso / altura**2


def categorizar_imc(imc):
    faixas = [
        (18.5, "abaixo do peso"),
        (25, "peso normal"),
        (30, "sobrepeso"),
        (float("inf"), "obesidade")
    ]

    return classificar_por_faixas(imc, faixas)


def classificar_pessoa(peso, altura):
    imc = calcular_imc(peso, altura)
    return categorizar_imc(imc)


def classificar_vento(velocidade):
    faixas = [
        (20, "calmo"),
        (40, "moderado"),
        (60, "forte"),
        (float("inf"), "tempestade")
    ]

    return classificar_por_faixas(velocidade, faixas)
