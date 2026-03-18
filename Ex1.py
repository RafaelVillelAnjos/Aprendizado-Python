# Use o método input para ler do teclado e informe se o número lido é positivo ou negativo.

num = float(input("Digite um número qualquer: "))

if num > 0:
    print(f"O número {num} é positivo.")
else:
    print(f"O número {num} é negativo.")