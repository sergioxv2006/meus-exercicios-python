# Lista que irá armazenar os dicionários de alunos.
alunos_cadastrados = []

# Laço de repetição principal que mantém o programa em execução.
while True:
    # Exibe o menu de opções para o usuário.
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1. Cadastrar Novo Aluno")
    print("2. Listar Alunos Cadastrados")
    print("3. Buscar Aluno por Matrícula")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    # --- 1. Cadastrar Novo Aluno ---
    if opcao == '1':
        print("\n--- Cadastro de Novo Aluno ---")
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")

        # Bloco para validar a matrícula.
        try:
            matricula_str = input("Digite o número de matrícula do aluno: ")
            matricula = int(matricula_str) # Tenta converter para número inteiro.

            # Cria o dicionário do aluno.
            aluno = {
                "nome": nome,
                "matricula": matricula,
                "curso": curso
            }

            # Adiciona o dicionário à lista.
            alunos_cadastrados.append(aluno)
            print(f"Aluno {nome} cadastrado com sucesso!")

        except ValueError:
            # Se a conversão para inteiro falhar, exibe um erro.
            print("Erro: A matrícula deve ser um número válido. Tente novamente.")

    # --- 2. Listar Alunos Cadastrados ---
    elif opcao == '2':
        print("\n--- Lista de Alunos Cadastrados ---")
        if not alunos_cadastrados:
            print("Nenhum aluno cadastrado ainda.")
        else:
            for aluno in alunos_cadastrados:
                print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Curso: {aluno['curso']}")

    # --- 3. Buscar Aluno por Matrícula ---
    elif opcao == '3':
        print("\n--- Buscar Aluno por Matrícula ---")
        if not alunos_cadastrados:
            print("Nenhum aluno cadastrado para buscar.")
        else:
            try:
                matricula_busca_str = input("Digite a matrícula que deseja buscar: ")
                matricula_busca = int(matricula_busca_str)

                aluno_encontrado = None
                for aluno in alunos_cadastrados:
                    if aluno['matricula'] == matricula_busca:
                        aluno_encontrado = aluno
                        break # Para a busca assim que encontrar o aluno.

                if aluno_encontrado:
                    print("Aluno encontrado:")
                    print(f"Nome: {aluno_encontrado['nome']}, Matrícula: {aluno_encontrado['matricula']}, Curso: {aluno_encontrado['curso']}")
                else:
                    print(f"Nenhum aluno encontrado com a matrícula {matricula_busca}.")

            except ValueError:
                print("Erro: A matrícula deve ser um número válido.")

    # --- 4. Sair ---
    elif opcao == '4':
        print("Saindo do programa. Até logo!")
        break # Interrompe o laço while e finaliza o programa.

    # --- Opção Inválida ---
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")