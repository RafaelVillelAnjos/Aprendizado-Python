# Refaça o exercício 8, apresentando todos os números separados por vírgula. Não pode haver vírgula no final.

num = int(input("Digite um número qualquer: "))
contador = 1

while contador <= num:
    if contador != num:
        print(contador, end=', ')
    else:
        print(contador, end=' ')

    contador += 1