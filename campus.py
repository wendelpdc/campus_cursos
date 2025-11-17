class Campus:
    def __init__(self, codigo, nome, endereco):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cursos = []
        
    def add_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            print(f"O curso '{curso}' foi adicionado ao campus {self.nome}.")
        else:
            print(f"O curso {curso} já existe no campus {self.nome}.")
        
    def listar_cursos(self):
        if self.cursos:
            print(f"Cursos presentes no campus {self.nome}: ")
            for curso in self.cursos:
                print(f"{curso}")
        else:
            print("Não há curso cadastrado no campus {self.nome}.")
            
def menu_interativo():
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
                campus.listar_cursos
    
        elif opcao == '4':
            print("Saindo...")
            break

if __name__ == "__main__":
    menu_interativo()

                
        