# main.py

projetos = []

def cadastrar_projeto():
    titulo = input("Digite o título do projeto: ")
    cliente = input("Digite o nome do cliente: ")
    prazo = input("Digite o prazo (dd/mm/aaaa): ")

    projeto = {
        "titulo": titulo,
        "cliente": cliente,
        "prazo": prazo,
        "status": "Aberto"
    }

    projetos.append(projeto)
    print("Projeto cadastrado com sucesso!\n")


def listar_projetos():
    if len(projetos) == 0:
        print("Nenhum projeto cadastrado.\n")
        return

    print("\n--- LISTA DE PROJETOS ---")
    for i in range(len(projetos)):
        p = projetos[i]
        print(f"{i+1}) {p['titulo']} | Cliente: {p['cliente']} | Prazo: {p['prazo']} | Status: {p['status']}")
    print("-------------------------\n")


def menu():
    while True:
        print("===== SISTEMA DE PROJETOS AMBIENTAIS =====")
        print("1 - Cadastrar projeto")
        print("2 - Listar projetos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_projeto()
        elif opcao == "2":
            listar_projetos()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.\n")


menu()
