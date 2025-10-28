# Sistema de Loja Virtual com Produtos Físicos e Digitais

from abc import ABC, abstractmethod

# Classe base abstrata
class Produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco_final(self):
        pass

# Produto Físico com custo de frete
class ProdutoFisico(Produto):
    def __init__(self, nome, preco_base, peso):
        super().__init__(nome, preco_base)
        self.peso = peso
        self.custo_frete = 10 if self.peso < 1 else 20

    def calcular_preco_final(self):
        return self.preco_base + self.custo_frete

# Produto Digital com taxa de serviço
class ProdutoDigital(Produto):
    def __init__(self, nome, preco_base, tamanho_arquivo):
        super().__init__(nome, preco_base)
        self.tamanho_arquivo = tamanho_arquivo
        self.taxa_servico = 5 if self.tamanho_arquivo < 100 else 15

    def calcular_preco_final(self):
        return self.preco_base + self.taxa_servico

# Carrinho de compras
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        return sum(produto.calcular_preco_final() for produto in self.produtos)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"{produto.nome}: R$ {produto.calcular_preco_final():.2f}")

# Teste do sistema
if __name__ == "__main__":
    print("=== Loja Virtual ===")
    carrinho = CarrinhoDeCompras()
    
    produto1 = ProdutoFisico("Livro", 50, 0.5)
    produto2 = ProdutoDigital("E-book", 30, 50)
    produto3 = ProdutoFisico("Smartphone", 800, 0.3)
    produto4 = ProdutoDigital("Curso Online", 200, 150)
    
    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    carrinho.adicionar_produto(produto3)
    carrinho.adicionar_produto(produto4)
    
    carrinho.listar_produtos()
    print(f"Total a pagar: R$ {carrinho.calcular_total():.2f}")

    print("\n=== Detalhes dos Produtos ===")
    print(f"Produto: {produto1.nome}, Preço Base: R$ {produto1.preco_base}, Peso: {produto1.peso}kg, Custo do Frete: R$ {produto1.custo_frete}")
    print(f"Produto: {produto2.nome}, Preço Base: R$ {produto2.preco_base}, Tamanho do Arquivo: {produto2.tamanho_arquivo}MB, Taxa de Serviço: R$ {produto2.taxa_servico}")
    print(f"Produto: {produto3.nome}, Preço Base: R$ {produto3.preco_base}, Peso: {produto3.peso}kg, Custo do Frete: R$ {produto3.custo_frete}")
    print(f"Produto: {produto4.nome}, Preço Base: R$ {produto4.preco_base}, Tamanho do Arquivo: {produto4.tamanho_arquivo}MB, Taxa de Serviço: R$ {produto4.taxa_servico}")