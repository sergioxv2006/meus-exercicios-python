print("====== Supermercado ======")

carrinho = []

print("COMANDOS DISPONÍVEIS: [adicionar], [listar], [finalizar]")

while True:
    comando = input("\nO que você deseja fazer? ").strip().lower()

    if comando == "finalizar":
        print("\nFinalizando a compra...")
        if not carrinho:
            print("Você não comprou nada.")
        else:
            total = sum(produto["preco"] for produto in carrinho)
            print("=== Itens comprados ===")
            for i, produto in enumerate(carrinho, start=1):
                print(f"{i}. {produto['nome']} - R$ {produto['preco']:.2f}")
            print(f"Total: R$ {total:.2f}")
        print("Obrigado pela compra!")
        break

    elif comando == "adicionar":
        nome_produto = input("Digite o nome do produto: ").strip()

        while True:
            try:
                preco_produto = float(input(f"Digite o preço de {nome_produto}: ").replace(',', '.'))
                if preco_produto < 0:
                    print("Preço não pode ser negativo. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Preço inválido. Digite um número válido, ex: 5.99")

        produto = {"nome": nome_produto, "preco": preco_produto}
        carrinho.append(produto)
        print(f"✅ Produto '{nome_produto}' adicionado ao carrinho.")

    elif comando == "listar":
        if not carrinho:
            print("Seu carrinho está vazio!")
        else:
            print("\n=== Itens no carrinho ===")
            for i, produto in enumerate(carrinho, start=1):
                print(f"{i}. {produto['nome']} - R$ {produto['preco']:.2f}")
            total = sum(produto["preco"] for produto in carrinho)
            print(f"Total até agora: R$ {total:.2f}")

    else:
        print("Comando inválido. Tente novamente. Comandos: [adicionar], [listar], [finalizar]")
