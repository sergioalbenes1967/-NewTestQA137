# Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2


def sutrair_dois_numeros(num1, num2):
    return num1 - num2


def multiplicar_doi_numeros(num1, num2):
    return num1 * num2


def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2


# Calcular testar a área de um quadrado
# A área = Lado **

# Calcular e testar a área de um retangulo
# Área = Lado1 * Lado2

# Calcular e testar a área de um triangulo
# Área = Lado1 * Lado2 / 2

# Calcular e testar a área do um círculo
# Area = Pi * raio ** 2

def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2

def calcular_volume_do_paralelograma(largura, comprimento, altura):
    return largura * comprimento * altura


if __name__ == '__main__':

    # Garçon _ Requisições / Chamjadas
    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')  # <-- prato

    resultado = sutrair_dois_numeros(7, 5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_doi_numeros(9, 9)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(9, 0)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponenciação é {resultado}')


def testar_somar_dois_numeros():
    # - 1* Etapa: Configurar / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # saida / Output
    resultado_esperado = 17

    # _ 2* Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3* Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_volume_do_paralelograma():
    # 1 - Configura
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    # 2 _ Execute
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)

    # 3 - Valida
    assert resultado_atual == resultado_esperado
