# Use o método input para ler dois números do teclado e informe qual número é o maior

num1 = float(input("Digite um número qualquer: "))
num2 = float(input("Digite outro número qualquer: "))

if num1 > num2:
    print(f"O número {num1} é maior que {num2}")
elif num1 < num2:
    print(f"O número {num2} é maior que {num1}")
else:
    print(f"Os dois números são iguais")