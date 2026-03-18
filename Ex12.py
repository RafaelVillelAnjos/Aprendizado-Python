# O usuário digita valores até deixar o input vazio. Quando isso acontecer, o sistema mostra todos os números pares.

repeticao = True
numsPares = []

while repeticao == True:
    num = input("Digite um número: ")

    if num != '':
        numFloat = float(num)
        if numFloat % 2 == 0:
            numsPares.append(numFloat)
    else:
        break

print(numsPares)