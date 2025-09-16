class Produto:

    def __init__(self, nome: str, preco: float, estoque: int):
        # RF01
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        print(f"Produto {self.nome} criado com o preço de R$ {self.preco} e estoque de {self.estoque} unidades")

        def aplicar_desconto(self, percent_desconto: float):
            # RF02
            desconto = self.preco * (percent_desconto / 100)
            novo_preco = self.preco - desconto
            
            # RFN01
            if novo_preco < 0:
                self.preco = 0.0
                print(f"[INFO] Desconto {percent_desconto} aplicado em {self.nome}.")
            else:
                self.preco = novo_preco
                print(f"[INFO] Desconto de {percent_desconto} aplicado em {self.nome}.")

        # RF03
        def verificar_estoque(self):
            return self.estoque > 0
        

# 1. Cria um objeto
notebook = Produto('Notebook', 4000, 10)
celular1 = Produto('Iphone 13', 3000, 10)
celular2 = Produto('Iphone 14', 5000, 10)
celular3 = Produto('Iphone 15', 8000, 10)
celular4 = Produto('Iphone 16', 10000, 10)
print(notebook.nome)
print(celular1.nome)
print(celular2.nome)
print(celular3.nome)
print(celular4.nome)