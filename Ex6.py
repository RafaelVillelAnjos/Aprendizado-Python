# Peça a idade e classifique a pessoa.
# 0–12 → Criança
# 13–17 → Adolescente
# 18 ou mais → Adulto

idadeUsuario = int(input("Digite sua idade (em anos): "))

if idadeUsuario >= 0 and idadeUsuario <= 12:
    print("Você é uma criança")
elif idadeUsuario > 12 and idadeUsuario <= 17:
    print("Você é um adolescente")
else:
    print("Você é um adulto")