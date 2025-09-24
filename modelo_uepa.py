class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        print(f"Olá! Sou um membro da comunidade UEPA. Meu nome é {self.nome}.")

class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso):
        super().__init__(nome, matricula, email)
        self.curso = curso

    def apresentar(self):
        print(f"Olá! Sou o aluno {self.nome}, do curso de {self.curso}. Minha matrícula é {self.matricula}.")

    def verificar_notas(self):
        print(f"Verificando as notas do aluno {self.nome}...")
        print("Notas verificadas com sucesso!")

class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento

    def apresentar(self):
        print(f"Olá! Sou o professor {self.nome}, do departamento de {self.departamento}. Meu e-mail é {self.email}.")

    def lancar_frequencia(self):
        print(f"Professor(a) {self.nome} está lançando a frequência dos alunos...")
        print("Frequência lançada com sucesso!")

# --- Área de Testes e Demonstração ---
if __name__ == "__main__":
    print(" --- Demonstração do Sistema UEPA Digital ---")

    # Criando uma instância de Aluno
    aluno1 = Aluno(
        nome = "Paulo Sérgio",
        matricula = "2309202501",
        email = "paulo.sergio@aluno.uepa.br",
        curso = "Ciência da Computação"
    )

    aluno2 = Aluno(
        nome = "Maria Beatriz",
        matricula = "2309202502",
        email = "maria.beatriz@aluno.uepa.br",
        curso = "Engenharia de Software"
    )

    # Criando uma instância de Professor
    professor1 = Professor(
        nome = "Rebeca Gonçalves",
        matricula = "2309202503",
        email = "rebeca.goncalves@professor.uepa.br",
        departamento = "DCCET - Departamento de Ciências e Tecnologia"
    )

    professor2 = Professor(
        nome = "Carlos Eduardo",
        matricula = "2309202504",
        email = "carlos.eduardo@professor.uepa.br",
        departamento = "DDCI - Departamento de Desenvolvimento de Sistemas e Informática"
    )

    print(f"\n--- Informações do Aluno ---")
    aluno1.apresentar()
    aluno1.verificar_notas()

    print()

    aluno2.apresentar()
    aluno2.verificar_notas()

    print(f"\n--- Informações do Professor ---")
    professor1.apresentar()
    professor1.lancar_frequencia()

    print()

    professor2.apresentar()
    professor2.lancar_frequencia()
