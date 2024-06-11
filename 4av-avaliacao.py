# 1° Questão

def reverter_numero(num):
    num_rev = num[-1::-1]
    return num_rev

numero = input("Digite um número: ")
numero_reverso = reverter_numero(numero)
print("O número invertido é:", numero_reverso)



# 2° Questão

# def tamanho_numero(num):
#     return len(num)

# numero = input("Digite um número: ")
# print("A quantidade de dígitos do número informado é: ", tamanho_numero(numero))



# 3° Questão (considerar b negativo)

# def potencia(a, b):
#     resultado = 1
#     if b < 0:
#         a = 1 / a
#         b = -b
#     for i in range(b):
#         resultado *= a
#     return resultado

# base = int(input("Digite o valor de a: "))
# expoente = int(input("Digiteo o valor de b: "))

# resultado = potencia(base, expoente)
# print("O resultado de", base, "elevado a", expoente, "é:", resultado)



# 4° Questão

# def maior(*valores):
#     maior_valor = valores[0]
#     for valor in valores:
#         if valor > maior_valor:
#             maior_valor = valor
#     return maior_valor

# entrada = input("Digite os valores separados por espaços: ")
# valores = [int(valor) for valor in entrada.split()]
# if valores:
#     print("O maior valor é:", maior(*valores))
# else:
#     print("Nenhum valor foi inserido.")