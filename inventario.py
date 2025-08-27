# inventario.py

print("--- Inventário de Itens ---")

inventario = []

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar inventário")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ").strip()

    if opcao == '1':
        nome = input("Nome do item: ").strip()
        if not nome:
            print("O nome do item não pode ser vazio.")
            continue
        try:
            quantidade = int(input("Quantidade: ").strip())
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número inteiro.")
            continue

        inventario.append({"nome": nome, "quantidade": quantidade})
        print(f"Item '{nome}' com quantidade {quantidade} adicionado ao inventário.")

    elif opcao == '2':
        nome = input("Digite o nome do item a ser removido: ").strip()
        removido = False
        for item in inventario:
            if item["nome"].lower() == nome.lower():
                inventario.remove(item)
                print(f"Item '{nome}' removido do inventário.")
                removido = True
                break
            if not removido:
                print(f"Item '{nome}' não encontrado no inventário.")

    elif opcao == '3':
        if inventario:
            print("\nItens no inventário:")
            for i, item in enumerate(inventario, 1):
                print(f"{i}. {item['nome']} - Quantidade: {item['quantidade']}")
        else:
            print("O inventário está vazio.")

    elif opcao == '4':
        print("Saindo do inventário.")
        break

    else:
        print("Opção inválida. Por favor, escolha entre 1 e 4.")