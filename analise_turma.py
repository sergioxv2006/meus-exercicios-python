# analise_turma.py

# Estrutura de dados inicial com a lista de alunos
alunos = [
    {"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},
    {"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},
    {"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},
    {"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},
    {"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},
    {"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0, "status_matricula": "ativo"},
    {"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},
    {"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"}
]

# analise_turma.py (continuação)

# 1. Filtrar alunos elegíveis
# A função filter() aplica a expressão lambda a cada aluno.
# Ela retorna um iterador com os alunos que atendem à condição:
# frequência >= 75.0 e status da matrícula é "ativo".
alunos_elegiveis = filter(
    lambda aluno: aluno["frequencia"] >= 75.0 and aluno["status_matricula"] == "ativo",
    alunos
)

# 2. Aplicar bônus de 10% na nota fiscal dos alunos elegíveis
# A função map() aplica a transformação do lambda em cada aluno da lista filtrada.
# A nova nota é calculada (nota * 1.1) e limitada a 10.0 usando a função min().
# Um novo dicionário é criado para cada aluno com a nota atualizada.
alunos_com_bonus = map(
    lambda aluno: {
        **aluno,  # Copia todos os dados do aluno original
        "nota_final": min(aluno["nota_final"] * 1.1, 10.0) # Calcula e limita a nova nota
    },
    alunos_elegiveis
)

# 3. Identificar os alunos destaque
# Filtramos novamente, agora para encontrar alunos cuja nota final, após o bônus,
# seja maior ou igual a 9.0.
alunos_destaque = filter(
    lambda aluno: aluno["nota_final"] >= 9.0,
    alunos_com_bonus
)

# 4. Saída Esperada: Imprimir o nome e a nota final dos alunos destaque
print("Alunos Destaque:")
for aluno in alunos_destaque:
    # Formata a nota para exibir com duas casas decimais
    nota_formatada = "{:.2f}".format(aluno["nota_final"])
    print(f"- Nome: {aluno['nome']}, Nota Final com Bônus: {nota_formatada}")