def adicionar_contato(contatos, nome, telefone, email):
    contatos.append({"nome": nome, "telefone": telefone, "email": email, "favorito": False})
    print(f"Contato {nome} adicionado com sucesso")
    return

def listar_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        favorito = ""
        if contato['favorito'] == True:
            favorito = "Sim"
        else:
            favorito = "Não"
        print(f"{indice} - Nome: {contato['nome']}, Telefone: {contato['telefone']}, Favorito: {favorito}")
    return

def listar_contatos_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato['favorito'] == True:
            favorito = "Sim"
            print(f"{indice} - Nome: {contato['nome']}, Telefone: {contato['telefone']}, Favorito: {favorito}")
    return

def editar_contato(contatos, indice, nome, telefone, email):
    contatos[indice]['nome'] = nome
    contatos[indice]['telefone'] = telefone
    contatos[indice]['email'] = email
    print(f"Contato {indice} editado com sucesso")
    return

def favoritar_contato(contatos, indice):
    contatos[indice]['favorito'] = True
    print(f"Contato {indice} favoritado com sucesso")
    return

def excluir_contato(contatos, indice):
    contatos.pop(indice)
    print(f"Contato {indice} excluído com sucesso")
    return

contatos = []

while True:
    print("1 - Adicionar contato")
    print("2 - Listar todos os contatos")
    print("3 - Listar contatos favoritos")
    print("4 - Editar contato")
    print("5 - Favoritar contato")
    print("6 - Excluir contato")
    print("7 - Sair")

    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        print("\nAdicionar contato:")
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif opcao == 2:
        print("\nLista de contatos:")
        listar_contatos(contatos)
    elif opcao == 3:
        print("\nEditar contato:")
        indice = int(input("Digite o índice do contato: "))
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        editar_contato(contatos, indice, nome, telefone, email)
    elif opcao == 4:
        print("\nFavoritar contato:")
        indice = int(input("Digite o índice do contato: "))
        favoritar_contato(contatos, indice)
    elif opcao == 5:
        print("\nExcluir contato:")
        indice = int(input("Digite o índice do contato: "))
        excluir_contato(contatos, indice-1)
    elif opcao == 6:
        print("\nLista de contatos favoritos:")
        listar_contatos_favoritos(contatos)
    elif opcao == 7:
        break