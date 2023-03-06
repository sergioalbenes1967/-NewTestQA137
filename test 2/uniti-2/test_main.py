import pytest

from main import somar_dois_numeros, calcular_area_do_circulo, calcular_volume_do_paralelograma


def testar_somar_dois_numeros():
    # - 1* Etapa: Configurar / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 4
    num2 = 5
    # saida / Output
    resultado_esperado = 9

    # _ 2* Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3* Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

    # anotação para utilizar como massa de teste


@pytest.mark.parametrize('raio,resultado_esperado', [
    # valoraes
    (1, 3.14),  # teste n°1
    (2, 12.56),  # teste n 2°
    (3, 28.26),  # teste n°3
    (4, 50.24),  # teste n°4

])
def testar_calcular_area_do_circulo(raio, resultado_esperado):
    # 1 - Configura / Comentamoms para que os parametros sejam lidos
    # raio = 2
    # resultado_esperado = 12.56

    # 2 - Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Valida
    assert resultado_atual == resultado_esperado


def testar_calcular_volume_do_paralelograma():
    # 1 - Configurar
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    # 2 - Executa
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)

    # 3 - Valida
    assert resultado_atual == resultado_esperado
