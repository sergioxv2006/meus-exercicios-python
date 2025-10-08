from abc import ABC, abstractmethod
from enum import Enum

class StatusItem(Enum):
    RECEBIDO = "Recebido"
    EM_PREPARO = "Em Preparo"
    PRONTO = "Pronto"

class StatusPedido(Enum):
    ABERTO = "Aberto"
    FECHADO = "Fechado"

class ItemMenu(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.__status = StatusItem.RECEBIDO

    def get_status(self):
        return self.__status.value
    
    def set_status(self, novo_status: StatusItem):
        self.__status = novo_status
        print(f"Status do item '{self.nome}' atualizado para: {self.get_status()}")

    @abstractmethod
    def descrever(self):
        pass

class Prato(ItemMenu):
    def __init__(self, nome, preco, tempo_preparo):
        super().__init__(nome, preco)
        self.tempo_preparo = tempo_preparo

    def descrever(self):
        return f"- Prato: {self.nome} (Preparo: {self.tempo_preparo} min) [{self.get_status()} - R$ {self.preco:.2f}]"
    
class Bebida(ItemMenu):
    def __init__(self, nome, preco, tamanho_ml):
        super().__init__(nome, preco)
        self.tamanho_ml = tamanho_ml

    def descrever(self):
        return f"- Bebida: {self.nome} (Tamanho: {self.tamanho_ml} mL) [{self.get_status()} - R$ {self.preco:.2f}]"
    
class Pedido:
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self._itens = []
        self.__status = StatusPedido.ABERTO
        self.__taxa_servico = 0.10 # 10% de taxa de serviço

    def adicionar_item(self, item: ItemMenu):
        if self.__status == StatusPedido.ABERTO:
            self._itens.append(item)
            print(f"Item '{item.nome}' adicionado ao pedido {self.id_pedido}.")
        else:
            print("Não é possível adicionar itens a um pedido fechado.")

    def alterar_status_item(self, indice_item, novo_status: StatusItem):
        if 0 <= indice_item < len(self._itens):
            self._itens[indice_item].set_status(novo_status)
            print(f"Status do pedido alterado para {self.novo_status}")
        else:
            print("Item não encontrado no pedido.")

    def calcular_subtotal(self):
        return sum(item.preco for item in self._itens)

    def exibir_comanda_cozinha(self):
        print(f"COMANDA PARA COZINHA | Pedido: {self.id_pedido}")
        for item in self._itens:
            print(item.descrever())

    def exibir_fatura(self):
        self.s__status = StatusPedido.FECHADO
        subtotal = self.calcular_subtotal()
        servico = subtotal * self.__taxa_servico
        total_a_pagar = servico + subtotal

        print(f"FATURA | PEDIDO: {self.id_pedido}")
        print(f"="*40)
        for item in self._itens:
            print(f"{item.nome} R$ {item.preco:.2f}")
        print(f"."*40)
        print(f"Subtotal: {subtotal}")
        print(f"Taxa de Serviço: {servico}")
        print(f"TOTAL A PAGAR: R$ {total_a_pagar:.2f}")
        print(f"="*40)

# Criar e testar o sistema
moqueca = Prato("Moqueca Baiana", 45.00, 30)
agua = Bebida("Água Mineral", 5.00, 500)
sorvete = Prato("Sorvete", 12.00, 10)

# Abrindo pedido e adicionando itens

pedido_mesa_01 = Pedido("mesa_01")
pedido_mesa_01.adicionar_item(moqueca)
pedido_mesa_01.adicionar_item(agua)
pedido_mesa_01.adicionar_item(sorvete)

# Exibir comanda para cozinha
pedido_mesa_01.exibir_comanda_cozinha()