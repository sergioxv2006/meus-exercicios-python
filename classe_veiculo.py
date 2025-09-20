# Definindo a classe base Veículo
class Automovel:

    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"Acelerando para {self.velocidade} km/h")

    def frear(self, valor):
        self.velocidade = max(0, self.velocidade - valor)
        print(f"Reduzindo para {self.velocidade} km/h")

    def info(self):
        print(f"Veículo: {self.marca} {self.modelo} ({self.ano}) - Velocidade atual: {self.velocidade} km/h")

    # Super

class Carro(Automovel):
        
        def __init__(self, marca: str, modelo: str, ano: int, portas: int):
            super().__init__(marca, modelo, ano)
            self.portas = portas

        def abrir_porta(self, numero: int):
            print(f"Abrindo a porta {numero}")

        def info(self):
            print(f"{super().info()} - {self.portas} portas")

class Moto(Automovel):
        
        def __init__(self, marca: str, modelo: str, ano: int, cilindradas: int):
            super().__init__(marca, modelo, ano)
            self.cilindradas = cilindradas
            
        def empinar(self):
            print("Empinando a moto!")

        def info(self):
            print(f"{super().info()} - Cilindradas: {self.cilindradas}")

carro_1 = Carro("Tesla", "Model S", 2022, 4)
carro_1.info()
moto_1 = Moto("Yamaha", "MT-07", 2021, 689)
moto_1.info()

# utilizando metodos
print("\n")
carro_1.abrir_porta(3)
carro_1.acelerar(20)
carro_1.frear(10)
print(carro_1.velocidade)

print("\n")
print(moto_1.velocidade)
moto_1.acelerar(40)
moto_1.frear(10)
print(moto_1.velocidade)
