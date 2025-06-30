import os
lista = []
while True:
    print("selecione uma opção:")
    opcao = input("1 - Adicionar um item\n2 - Listar os itens\n3 - Apagar um item\n4 - Sair\n")
    if opcao == "1":
        os.system('cls')
        item = input("Digite o item a ser adicionado: ")
        lista.append(item)
        print(f"Item '{item}' adicionado com sucesso!")
    elif opcao == "2":
        os.system('cls')
        if lista:
            print("Itens na lista:")
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")
        else:
            print("A lista está vazia.")
    elif opcao == "3":
        os.system('cls')
        if lista:
            item_num = input("Digite o número do item a ser apagado: ")
            try:
                index = int(item_num) - 1
                if 0 <= index < len(lista):
                    removed_item = lista.pop(index)
                    print(f"Item '{removed_item}' apagado com sucesso!")
                else:
                    print("Número do item inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
        else:
            print("A lista está vazia.")
    elif opcao == "4":
        os.system('cls')
        print("Saindo do programa...")
        break
    else:
        os.system('cls')
        print("Opção inválida. Por favor, tente novamente.")