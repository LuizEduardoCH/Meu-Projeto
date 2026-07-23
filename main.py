from Pedido import Pedido
from Prato import Prato
from Bebida import Bebida
from Sobremesa import Sobremesa

# Programa principal
idade = int(input("Digite sua idade: "))
pedido = Pedido(idade >= 18)

while True:
    print("\n====== CARDÁPIO ======")
    print("1 - Arroz e Feijão - R$25")
    print("2 - Lasanha - R$40")
    print("3 - Parmegiana - R$35")
    print("4 - Cerveja - R$8")
    print("5 - Refrigerante - R$6")
    print("6 - Sobremesas")
    print("7 - Finalizar pedido")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pedido.adicionar_item(Prato("Arroz e Feijão", 25, "simples"))
        print("Item adicionado!")

    elif opcao == "2":
        pedido.adicionar_item(Prato("Lasanha", 40, "elaborada"))
        print("Item adicionado!")

    elif opcao == "3":
        pedido.adicionar_item(Prato("Parmegiana", 35, "media"))
        print("Item adicionado!")

    elif opcao == "4":
        if pedido.adicionar_item(Bebida("Cerveja", 8, True)):
            print("Item adicionado!")

    elif opcao == "5":
        if pedido.adicionar_item(Bebida("Refrigerante", 6, False)):
            print("Item adicionado!")

    elif opcao == "6":
        while True:
            print("\n====== SOBREMESAS ======")
            print("1 - Pudim - R$12")
            print("2 - Sorvete - R$10")
            print("3 - Mousse de Maracujá - R$15")
            print("4 - Voltar")

            opcao_sobremesa = input("Escolha uma sobremesa: ")

            if opcao_sobremesa == "1":
                pedido.adicionar_item(Sobremesa("Pudim", 12))
                print("Sobremesa adicionada!")

            elif opcao_sobremesa == "2":
                pedido.adicionar_item(Sobremesa("Sorvete", 10))
                print("Sobremesa adicionada!")

            elif opcao_sobremesa == "3":
                pedido.adicionar_item(Sobremesa("Mousse de Maracujá", 15))
                print("Sobremesa adicionada!")

            elif opcao_sobremesa == "4":
                break

            else:
                print("Opção inválida!")

    elif opcao == "7":
        break

    else:
        print("Opção inválida!")

pedido.aplicar_brinde()
pedido.mostrar_pedido()