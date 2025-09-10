import sys

operacoes = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x - y,
    '3': lambda x, y: x * y,
    '4': lambda x, y: x / y if y != 0 else "Não existe divisão por zero"
}

while True:
    print("O que você deseja fazer?")
    print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Sair")
    op = input("Opção: ")

    if op in operacoes:
        x = float(input("Digite seu primeiro número: "))
        y = float(input("Digite seu segundo número: "))

        r = operacoes[op](x, y)

        print(f"O resultado é: {r}\n")
    elif op == '5':
        print("Saindo...")
        sys.exit(0)