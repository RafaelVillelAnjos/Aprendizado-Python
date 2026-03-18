# Detector de repetição. O usuário pode digitar quantos valorws quiser. Ao inserir um valor vazio, o sistema mostra a primeira repetição.


listaNums = []
repetidos = []

while True:
    num = input("digite um número: ")
    if num == '':
        break
    numInt = int(num)

    if numInt in listaNums:
        repetidos.append(numInt)
    else: 
        listaNums.append(numInt)

print(repetidos[0])

