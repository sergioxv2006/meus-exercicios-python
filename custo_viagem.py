# Planejador de Custo de Viagem
print("--- Planejador de Custo de Viagem ---")

distancia = float(input("Digite a distância da viagem em km:"))
consumo = float(input("Digite o consumo do veículo em km/litro:"))
preco_combustivel = float(input("Digite o preço do combustível por litro: R$"))

custo_viagem = (distancia / consumo) * preco_combustivel

print("\n--- Resultado ---")
print(f"O custo total da viagem é: R$ {custo_viagem:.2f}")