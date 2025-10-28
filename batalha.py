# Importando ABC (Abstract Base Class) e abstractmethod para criar a classe abstrata
from abc import ABC, abstractmethod
import random

# --- CLASSE BASE ABSTRATA ---
class Personagem(ABC):
    """
    Classe base abstrata para todos os personagens do jogo.
    """
    def __init__(self, nome: str, vida: int, ataque_base: int):
        self.nome = nome   # Atributo público
        self._vida = vida   # Atributo protegido
        self._ataque_base = ataque_base   # Atributo protegido

    @property
    def vida(self):
        """Getter para o atributo vida, permitindo acesso controlado."""
        return self._vida
    
    # Método para receber dano, garantindo que a vida não fique negativa (Encapsulamento).
    def receber_dano(self, dano: int):
        """
        Reduz a vida do personagem com base no dano recebido.
        A vida nunca será menor que zero.
        """
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"{self.nome} recebeu {dano} de dano e agora tem {self._vida} de vida.")

    # Método para verificar se o personagem ainda está vivo.
    def esta_vivo(self) -> bool:
        """
        Retorna True se a vida do personagem for maior que zero.
        """
        return self._vida > 0
    
    # Método abstrato que força as subclasses a implementarem sua própra lógica de ataque (Abstração).
    @abstractmethod
    def atacar(self, alvo: 'Personagem'):
        """
        Método de ataque que deve ser implementado por todas as subclasses.
        Este é o "contrato" da classe Personagem.
        """
        pass

# --- CLASSES DERIVADAS (HERANÇA) ---

# Classe Guerreiro, que herda de Personagem.
class Guerreiro(Personagem):
    """
    Classe que representa um Guerreiro. Herda de Personagem e adiciona
    mecânicas de fúria para ataques especiais.
    """
    def __init__(self, nome: str, vida: int, ataque_base: int, furia: int = 20):
        # Utilizando super() para chamar o construtor da classe mãe (Personagem).
        super().__init__(nome, vida, ataque_base)
        self.__furia = furia # Atributo privado (private) para encapsular a fúria.

    # Implementação do método atacar para o Guerreiro (Polimorfismo).
    def atacar(self, alvo: Personagem):
        """
        Ataque padrão do Guerreiro que causa dano ao alvo e gera fúria.
        """
        dano = self._ataque_base + random.randint(1, 6) # Dano base + um fator aleatório
        print(f"🗡️ {self.nome} ataca {alvo.nome} com sua espada!")
        alvo.receber_dano(dano)
        self.__furia += 10 # Gera fúria a cada ataque normal
        print(f"{self.nome} gerou 10 de fúria. Fúria atual: {self.__furia}")

    # Método específico do Guerreiro que consome fúria (Encapsulamento).
    def ataque_especial(self, alvo: Personagem):
        """
        Ataque especial que consome fúria para causar um dano maior.
        A lógica da fúria está encapsulada e protegida.
        """
        custo_furia = 25
        if self.__furia >= custo_furia:
            print(f"🔥 {self.nome} usa ATAQUE ESPECIAL FURIOSO contra {alvo.nome}!")
            dano_especial = int(self._ataque_base * 1.8) # Dano aumentado
            alvo.receber_dano(dano_especial)
            self.__furia -= custo_furia # Consome o recurso
            print(f"{self.nome} consumiu {custo_furia} de fúria. Fúria restante: {self.__furia}")
        else:
            print(f"{self.nome} tentou usar o ataque especial, mas não tem fúria suficiente! Atacando normalmente.")
            self.atacar(alvo) # Se não tiver fúria, realiza um ataque normal

# Classe Mago, que herda de Personagem.
class Mago(Personagem):
    """
    Classe que representa um Mago. Herda de Personagem e utiliza mana
    para lançar magias.
    """
    def __init__(self, nome: str, vida: int, ataque_base: int, mana: int = 100):
        # Utilizando super() para chamar o construtor da classe mãe.
        super().__init__(nome, vida, ataque_base)
        self.__mana = mana # Atributo privado para encapsular a mana.

    # Implementação do método atacar para o Mago (Polimorfismo).
    def atacar(self, alvo: Personagem):
        """
        Ataque mágico do Mago que consome mana para causar dano.
        A gestão da mana é encapsulada.
        """
        custo_mana = 20
        if self.__mana >= custo_mana:
            dano = self._ataque_base + random.randint(5, 10) # Dano mágico é mais consistente
            print(f"🔮 {self.nome} lança uma bola de fogo em {alvo.nome}!")
            alvo.receber_dano(dano)
            self.__mana -= custo_mana # Consome mana
            print(f"{self.nome} gastou {custo_mana} de mana. Mana restante: {self.__mana}")
        else:
            # Se não tiver mana, o mago causa um dano físico muito menor
            print(f"{self.nome} não tem mana suficiente! Ataca com seu cajado.")
            dano_fisico = int(self._ataque_base / 3)
            alvo.receber_dano(dano_fisico)


# --- SIMULAÇÃO DA BATALHA ---
# O código abaixo cria as instâncias e simula a batalha em turnos.
if __name__ == "__main__":
    # 1. Criação das instâncias dos personagens
    guerreiro = Guerreiro(nome="Aragorn", vida=120, ataque_base=15)
    mago = Mago(nome="Gandalf", vida=80, ataque_base=20)

    print("--- 💥 INÍCIO DA BATALHA 💥 ---")
    print(f"{guerreiro.nome} (Vida: {guerreiro.vida}) vs {mago.nome} (Vida: {mago.vida})\n")

    turno = 1
    # 2. Laço de repetição que continua enquanto ambos estiverem vivos. 
    while guerreiro.esta_vivo() and mago.esta_vivo():
        print(f"--- ⚔️ TURNO {turno} ⚔️ ---")

        # Turno do Guerreiro
        print(f"É a vez de {guerreiro.nome} atacar!")
        # Lógica simples: Se tiver fúria, chance de usar especial.
        if random.random() < 0.4: # 40% de chance de tentar usar o especial
             guerreiro.ataque_especial(mago)
        else:
             guerreiro.atacar(mago)
        
        print("-" * 20)

        # Verifica se o Mago sobreviveu antes de atacar
        if not mago.esta_vivo():
            break

        # Turno do Mago
        print(f"É a vez de {mago.nome} atacar!")
        mago.atacar(guerreiro)
        
        print("\n--- RESUMO DO TURNO ---")
        print(f"Vida de {guerreiro.nome}: {guerreiro.vida}")
        print(f"Vida de {mago.nome}: {mago.vida}\n")

        turno += 1

    # 3. Fim da batalha e anúncio do vencedor
    print("--- 🏆 FIM DA BATALHA 🏆 ---")
    if guerreiro.esta_vivo():
        print(f"O grande vencedor é {guerreiro.nome}!")
    else:
        print(f"O grande vencedor é {mago.nome}!")