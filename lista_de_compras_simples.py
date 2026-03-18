def exibir_menu():
    print("\n" + "=" * 50)
    print("Bem vindo à Lista de Compras Simples!")
    print("\n")


def listar_produtos(produtos):
    print("\nItems na Lista de Compras:")
    if not produtos:
        print("A lista está vazia.")
    else:
        # Mostrar tabela simples para visualização
        print(f"{'ID':<4} | {'Nome':<15} | {'Qtd':<8} | {'Descrição'}")
        print("-" * 50)
        for p in produtos:
            print(f"{p['id']:<4} | {p['nome']:<15} | {p['quantidade']:<8} | {p['descricao']}")
    print("-" * 50)


def adicionar_produto(lista_compras, proximo_id):
    nome = ""
    quantidade = 0.0
    descricao = ""
    novo_produto = {}

    try:
        nome = input("Nome do produto: ").strip()

        quantidade = float(input("Quantidade: "))
        descricao = input("Descrição do produto: ")

        novo_produto = {
            "id": proximo_id,
            "nome": nome,
            "quantidade": quantidade,
            "descricao": descricao
        }

        lista_compras.append(novo_produto)
        print(f"\n[SUCESSO] Produto '{nome}' adicionado com ID {novo_produto['id']}.")
        return proximo_id + 1

    except ValueError:
        print("\n[ERRO] Entrada inválida! Quantidade deve ser um número.")
        return proximo_id


def remover_produto(lista_compras):
    id_remover = 0
    removido = False
    i = 0
    p = {}

    try:
        id_remover = int(input("Digite o ID do produto que deseja remover: "))
        removido = False

        for i, p in enumerate(lista_compras):
            if p['id'] == id_remover:
                del lista_compras[i]
                removido = True
                break

        if removido:
            print(f"\n[SUCESSO] Produto com ID {id_remover} removido.")
        else:
            print(f"\n[AVISO] ID {id_remover} não encontrado.")
    except ValueError:
        print("\n[ERRO] Digite um número de ID válido.")


def pesquisar_produtos(lista_compras):
    termo = ""
    resultados = []

    termo = input("Digite o nome ou parte do nome para pesquisar: ").lower()
    resultados = [p for p in lista_compras if termo in p['nome'].lower()]

    print(f"\n--- RESULTADOS DA PESQUISA ({len(resultados)} encontrados) ---")
    if resultados:
        for r in resultados:
            print(f"ID: {r['id']} | Nome: {r['nome']} | Qtd: {r['quantidade']}")
    else:
        print("Nenhum produto encontrado com esse nome.")


def main():
    lista_compras = []
    proximo_id = 1
    opcao = ""

    exibir_menu()

    while True:
        print("\nMENU DE OPÇÕES:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Exibir lista de items")
        print("4. Pesquisar items")
        print("5. Sair do programa")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            proximo_id = adicionar_produto(lista_compras, proximo_id)

        elif opcao == '2':
            remover_produto(lista_compras)

        elif opcao == '3':
            listar_produtos(lista_compras)

        elif opcao == '4':
            pesquisar_produtos(lista_compras)

        elif opcao == '5':
            print("\nEncerrando o programa... Até logo!")
            break

        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()