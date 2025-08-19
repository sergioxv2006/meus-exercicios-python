# Planejador de Custo de Viagem
print("--- Planejador de Custo de Viagem ---")

try:
    distancia = int(input("Digite a distância da viagem em km: "))
    preco_gasolina = float(input("Digite o preço do litro da gasolina: "))
    consumo = float(input("Digite o consumo do veículo em km/litro: "))

    if distancia <= 0 or preco_gasolina <= 0 or consumo <= 0:
        raise ValueError("Os valores devem ser positivos.")
    else:
        custo_viagem = (distancia / consumo) * preco_gasolina
    print(f"O custo total da viagem é: R$ {custo_viagem:.2f}")
except ValueError as e:
    print(f"Erro: {e}. Por favor, insira valores válidos.")