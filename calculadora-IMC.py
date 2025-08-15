peso = float(input("Qual é o seu peso(kg)?"))
altura = float(input("Qual é a sua altura(m)?"))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")