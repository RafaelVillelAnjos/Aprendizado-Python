# Peça dois números, uma operação e mostre seu resultado
# ex: número 1: 10
# número 2: 3
# operação: *
# resultado: 30

print("Calculadora simples:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar com os dois números (+, -, * ou /): ")
resultado = 0

if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
    print(f"Número 1: {num1} \nNúmero 2: {num2} \nOperação: {operacao} \nConta: {num1} {operacao} {num2}")
else:
    print("Operação inválida! Tente novamente.")

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    resultado = num1 / num2
    print(f"Resultado: {resultado}")