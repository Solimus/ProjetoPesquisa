import os # modulo os fornece funções para interagir com sistema operacional

#função carrega arquivo de contatos se tiver algum
def carregar_contatos():
    contatos = {}
    if os.path.exists("contatos.txt"):
        with open("contatos.txt", "r") as arquivo:
            for linha in arquivo: #adiciona os contatos em uma linha
                nome, telefone, email = linha.strip().split(",")

                return contatos # retornar a linha


def salvar_contatos(contatos):
    with open("contatos.txt" "w") as arquivos:
        for nome, dados in contatos.items():
            arquivo.write(f"{nome};{dados['telefone']};{dados['email']}\n")

                    #função adicionar um contato
def adicionar_contatos(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    contatos[nome] = {"telefone": telefone, "email": email}
    print(f"Contato {nome} adicionado com sucesso!")


#função para remover um contato

def remover_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ")
    if nome in contatos: #se tiver o contato, então remove
        del contatos[nome]
        print(f"Contato{nome} removido com sucesso!")
    else:
        print("Contato não encontrado")


def atualizar_contato(Contato):
    nome = input("Digite o nome do contato a ser atualizado: ")
    if nome in  contatos:
        telefone = input("Digite o novo telefone: ")
        email = input("Digite o novo email: ")
        contatos[nome] = {"telefone": telefone, "email": email}
        print(f"Contatos {nome} atualizado com sucesso!")
    else:
        print("Nenhum contato cadastrado. ")


def exibir_contatos(contato):
    if contatos:
        for nome, dados in contatos>itens():
            print(f"Nome: {nome}, telefone: {dados[telefone]}, email: {dados['1email']}")
        else:
            print("Nenhum contato cadastrado.")


    def menu():
        contatos = carregar_contatos()

        while True:
            print("\n 1. Adicionar contato")
            print("2. Remover contato")
            print("3. Atualizar contato")
            print("4. Exibir contato")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                adicionar_contatos(contatos)
            elif opcao == "2":
                remover_contato(contatos)
            elif opcao == "3":
                atualizar_contato(contatos)  
            elif opcao == "4":
                exibir_contatos(contatos)
            elif opcao == "5":
                salvar_contatos(contatos)
                print("Contatos salvos. Saindo do programa.")
                break
            else:
                print("Opção inválida, tente novamente")



                if __name__ == "__main__":
                    menu()  
