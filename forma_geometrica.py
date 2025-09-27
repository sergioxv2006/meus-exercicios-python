from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def gerar_relatorio(formas):
    print("\nRELATÓRIO DE FORMAS GEOMÉTRICAS")

    for i, forma in enumerate(formas):
        area = forma.calcular_area()
        p = forma.calcular_perimetro()
        print(f"\nForma {i+1}: {forma.__class__.__name__}")
        print(f"Área: {area}, Perímetro: {p}")

    area_total = sum(forma.calcular_area() for forma in formas)
    p_total = sum(forma.calcular_perimetro() for forma in formas)

    print(f"\nÁREA TOTAL: {area_total}, PERÍMETRO TOTAL: {p_total}")


# Retângulo
r = Retangulo(10,20)
a_retangulo = r.calcular_area()
p_retangulo = r.calcular_perimetro()
print(f"A área do retângulo é {a_retangulo}")
print(f"O perímetro do retângulo é {p_retangulo}")

# Círculo
c = Circulo(10)
a_circulo = c.calcular_area()
p_circulo = c.calcular_perimetro()
print(f"A área do retângulo é {a_circulo}")
print(f"O perímetro do retângulo é {p_circulo}")

# Quadrado
q = Quadrado(10)
a_quadrado = q.calcular_area()
p_quadrado = q.calcular_perimetro()
print(f"A área do retângulo é {a_quadrado}")
print(f"O perímetro do retângulo é {p_quadrado}")

# Relatório
gerar_relatorio([r, c, q])