# Converta a temperatura para Fahrenheit

import time

temperaturaC = float(input("Digite uma temperatura em Celsius (apenas o número): "))

print('Calculando...')
time.sleep(100)

temperaturaF = (temperaturaC * 9/5) + 32

print(f"{temperaturaC} graus Celsius é igual a {temperaturaF} graus Fahrenheit")