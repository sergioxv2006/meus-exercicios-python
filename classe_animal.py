class Animal:
    def __init__(self, especie, nome, idade):
        self.especie = especie
        self.nome = nome
        self.idade = idade
        self.vivo = True
        self.fome = 50

    def comer(self):
        if self.vivo:
            self.fome += 10
            return f"{self.nome} comeu."
        else:
            return f"O animal não pode comer"
        
    def dormir(self):
        if self.vivo and self.fome > 30:
            self.fome -= 20
            return f"{self.nome} está dormindo"
        else:
            return f"{self.nome} está com fome e não pode dormir"
    
    def emitir_som(self):
        if self.vivo:
            return f"{self.nome} emite um som."
        else:
            return f"{self.nome} está morto e não pode emitir som."
        
    def mover(self):
        if self.vivo:
            return f"{self.nome} está se movendo"
        else:
            return f"{self.nome} está morto e não pode se mover"
        
nome = input("Digite o nome do animal: ")
especie = input("Digite a espécie do animal: ")
idade = int(input("Digite a idade do animal: "))

animal = Animal(especie, nome, idade)

print(animal.comer())
print(animal.dormir())
print(animal.emitir_som())
print(animal.mover())
print(f"Nome: {animal.nome}, Espécie: {animal.especie}, Idade: {animal.idade}, Vivo: {animal.vivo}, Fome: {animal.fome}")