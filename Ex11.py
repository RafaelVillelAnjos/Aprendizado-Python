# Calculadora de média. O usuário pode escrever quantos valores quiser. Quando o usário não informar o valor, o programa exibe a média dos valores informados

repeticao = True
contador = 0
somaNums = 0

while repeticao == True:
    num = input("Digite um número qualquer: ")

    if num != '':
        numFloat = float(num)
        somaNums += numFloat
        contador += 1
    else:
        repeticao = False

media = somaNums / contador
print(f"A média dos números digitados é {media}")
