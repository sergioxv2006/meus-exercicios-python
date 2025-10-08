from abc import ABC, abstractmethod

class ContaBancaria(ABC): # classe abstrata
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito Realizado no valor de R${valor:.2f},00")

    def get_saldo(self): #getter
        return self.__saldo
        
    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(ContaBancaria): # classe concreta

    def __init__(self, saldo_inicial=0, taxa_operacao=1.50):

        super().__init__(saldo_inicial)
        self.__taxa_operacao = taxa_operacao

    def sacar(self, valor):
        custo_total = valor + self.__taxa_operacao
        if valor > 0 and self.get_saldo() >= custo_total:
            novo_saldo = self.get_saldo() - custo_total
            self._ContaBancaria__saldo = novo_saldo
            print(f"Saque de R$ {valor:.2f} realizado na Conta Corrente. Saldo restante: R$ {self.get_saldo():.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque na Conta Corrente.")

class ContaPoupanca(ContaBancaria): # classe concreta

    def __init__(self, saldo_inicial=0, taxa_juros=0.1):

        super().__init__(saldo_inicial)
        self.__taxa_juros = taxa_juros

    def sacar(self, valor):
        if valor > 0 and self.get_saldo() >= valor:
            novo_saldo = self.get_saldo() - valor
            self._ContaBancaria__saldo = novo_saldo
            print(f"Saque de R$ {valor:.2f} realizado na Conta Poupança. Saldo restante: R$ {self.get_saldo():.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque na Conta Poupança.")

    def aplicar_juros(self):

        juros = self.get_saldo() * self.__taxa_juros
        self.depositar(juros)
        print(f"Juros de R$ {juros:.2f} aplicados na Conta Poupança. Novo saldo: R$ {self.get_saldo():.2f}")

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.__contas = []

    def adicionar_conta(self, conta: ContaBancaria):
        self.__contas.append(conta)
        print(f"Conta do tipo {type(conta).__name__} adicionada para o cliente {self.nome}.")

# Criando clientes e contas
cl_odete = Cliente("Odete Almeida Roitman")
cl_odete.adicionar_conta(ContaPoupanca(10000))
cl_odete.adicionar_conta(ContaCorrente())

conta1 = ContaPoupanca(1000)

cl_fatima = Cliente("Maria de Fátima")
cl_fatima.adicionar_conta(ContaCorrente(8000))
cl_fatima.adicionar_conta(ContaPoupanca(5000))

conta2 = ContaCorrente(500)

# Sacar 

conta1.sacar(200) 
conta2.sacar(100)
