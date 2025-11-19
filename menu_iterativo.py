from cursos import Campus

class MenuIterativo:
    def menu_iterativo():
        campus = None
        
        while True:
            print("***************")
            print("* MENU CAMPUS *")
            print("***************")

            print("1 - Criar campus")
            print("2 - Adicionar curso")
            print("3 - Listar cursos")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                codigo = int(input("Dgite o código do campus: "))
                nome = input("Digite o nome do campus: ")
                endereco = input("Digite o endereço do campus: ")
                campus = Campus(codigo, nome, endereco)
                print(f"Campus {nome} criado com sucesso.")
            
            elif opcao == '2':
                if campus is None:
                    print("Crie um campus primeiro.")
                else:
                    curso = input("Digite o nome do curso para que possa ser adicionado: ")
                    campus.add_curso(curso)
            
            elif opcao == '3':
                if campus is None:
                    print("Crie um campus primeiro.")
                else:
                    campus.listar_cursos()
        
            elif opcao == '4':
                print("Saindo...")
                break

if __name__ == "__main__":
    menu = MenuIterativo()
    menu.menu_iterativo()
